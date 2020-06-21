from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import User, TopInfo
from django.core.cache import cache


# Create your views here.


def flush():
    """刷新Top"""
    us = User.objects.all()
    dic = dict()
    for u in us:
        dic[u.T_id.num] = u.T_id.score
    # 通过字典的值进行排序（分数降序）
    info = sorted(zip(dic.values(), dic.keys()), reverse=True)
    # 统计用户数量
    count = User.objects.all().count()
    for c in range(count):
        # 修改Top数据
        TopInfo.objects.filter(num=info[c][1]).update(top=c + 1)
    return True


# def test(request):
#     import random
#     if request.method == 'GET':
#         for u in range(1, 11):
#             num = str(u)
#             user = 'user{}'.format(u)
#             pwd = '123456'
#             score = random.randint(1, 10000000)
#             TopInfo.objects.create(num=num, score=score)
#             User.objects.create_user(username=user, password=pwd, T_id_id=u)
#             print('完成{}条！'.format(u))
#             flush()
#         return HttpResponse('创建测试数据')


class Login(View):
    """登录"""

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if not all([username, password]):
            mes = {'mes': '请正确登录！'}
            return render(request, 'login.html', mes)
        if user:
            auth.login(request, user)
            return redirect('/')
        mes = {'mes': '账号密码错误!'}
        return render(request, 'login.html', mes)


def logout(request):
    """注销"""
    auth.logout(request)
    return redirect('api:login')


@method_decorator(login_required(login_url='login/'), name='dispatch')
class ShowInfo(View):
    """Top排行榜"""

    def get(self, request):
        """展示数据"""
        user = request.user
        info = TopInfo.objects.all().order_by('top')
        li_info = [[i.top, '客户端{}'.format(i.num), i.score] for i in info]
        # 存入redis中
        cache.set('Top', li_info)
        # print('Top:{}'.format(i.top), '客户端{}'.format(i.num), '分数{}'.format(i.score))
        # print(user.T_id.top, user.T_id.num, user.T_id.score)
        # return JsonResponse({'user': '客户端{}'.format(user.T_id.num)})
        return render(request, 'showinfo.html', {
            'info': li_info,
            'user': user
        })

    def post(self, request):
        """Top查询"""
        try:
            start = request.POST.get('start')
            end = request.POST.get('end')
            lis = cache.get('Top')
            if int(start) == 0:
                start = 1
            if int(end) > int(start) > 0:
                restful = lis[int(start) - 1:int(end)]
                # print(restful)
                return render(request, 'showinfo.html', {'restful': restful})
            else:
                return render(request, 'showinfo.html', {'mes': '输入有误！'})
        except Exception:
            return render(request, 'showinfo.html', {'mes': '输入有误！'})


@method_decorator(login_required(login_url='login/'), name='dispatch')
class UpInfo(View):
    """上传数据"""

    def get(self, request):
        return render(request, 'upinfo.html')

    def post(self, request):
        try:
            user = request.user
            score = request.POST.get('up_score')
            score_ = int(score)
            # 分数限制在1~10000000之间
            if 0 <= score_ <= 10000000:
                TopInfo.objects.filter(id=user.T_id_id).update(score=score_)
                flush()
                return render(request, 'upinfo.html', {'mes': '上传成功！'})
            else:
                return render(request, 'upinfo.html', {'mes': '输入的分数超出范围！'})
        except Exception:
            return render(request, 'upinfo.html', {'mes': '请输入1~10000000范围内整数！'})
