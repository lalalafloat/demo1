#-*- coding:utf-8 -*- #  
if __name__ == '__main__':
    print "sdsd {}".format("xc"),  #在输出的末尾加空格可以不换行输出 否在自带换行
    print "xxx"
    print "xcv"
    a = 10
    b = [1,2,3,4,10 ]
    print a in b
    a = [1,2, 3]
    b = [a,1,2]
    print a == b[0] #== 判断两个变量内容是否相同
    print a is b[0] #is 判断两个变量引用地址是否相同