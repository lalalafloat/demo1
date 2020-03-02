#-*- coding:utf-8 -*- #
import random

if __name__ == '__main__':
    for i in range(10, 0, -1): #左闭右开
        print i
    lst = list(range(10))
    random.shuffle(lst)
    print lst
    print random.sample(lst, min(len(lst),5)) #一次性取不重复的几个 取样不放回
    print random.randint(2,4) #[2,4]
    print random.randrange(2,4) #[2,4)