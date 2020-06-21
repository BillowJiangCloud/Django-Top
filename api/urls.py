from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # path('', views.test, name='test'),
    path('', views.ShowInfo.as_view(), name='index'),
    path('upinfo/', views.UpInfo.as_view(), name='UpInfo'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout')
]
