#-*- coding:utf-8 -*-
import random

rand_num = random.randrange(10)
count = 0

while count < 3:
    guess_num = int(input('请输入您猜测的数字(1~10):'))
    if guess_num > 10:
        print('您输入的数字超出范围了:1~10')
    elif guess_num == rand_num:
        print('哇~,太棒了你猜对了~')
        break
    elif guess_num < rand_num:
        print('您猜的数字有点小了,请尝试大点的数字')
    else:
        print("你猜的数字有点大了，请尝试小点的数字")
    count += 1
else:
    print("不要灰心你，这次只是运气不好，请下次尝试")

print("这个真正的数字是：%d" % rand_num)