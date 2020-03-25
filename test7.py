#-*- coding:utf-8 -*- #
class module(object):
    def __init__(self, num, lis):
        self.num = num
        self.lis = lis

if __name__ == '__main__':
    a = []
    a.append(module(1,[2,3]))
    a.append(module(4,[5,6]))
    for i in a:  #循环可以修改里面的元素
        i.num = 3
        i.lis.append(4)
    for i in a:
        print i.num, i.lis