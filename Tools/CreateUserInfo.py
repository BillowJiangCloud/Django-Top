import random

for u in range(1, 10):
    num = str(u)
    user = 'user{}'.format(u)
    pwd = '123456'
    score = random.randint(1, 10000000)
    print(num, user, pwd, score)
