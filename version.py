ver1 = input('v1:')
ver2 = input('v2:')


class Solution:
    def compareVersion(self, version1, version2):
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        v1_len = len(v1)
        v2_len = len(v2)

        # 小级版本号用0补充
        max_len = max(v1_len, v2_len)
        v1 += [0] * (max_len - v1_len)
        v2 += [0] * (max_len - v2_len)
        # print(max_len)

        if v1 > v2:
            print('结果：{}'.format(1))
            return 1
        elif v1 < v2:
            print('结果：{}'.format(-1))
            return -1
        else:
            print('结果：{}'.format(0))
            return 0


res = Solution()
Solution.compareVersion(res, version1=ver1, version2=ver2)
