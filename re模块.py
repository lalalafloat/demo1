#-*- coding:utf-8 -*- #
import re

if __name__ == '__main__':
    a = "奥迪A4首付3000元起"
    b = re.findall('\d+', a)
    print b[-1]
    c = [u'元', u'利息', u'息']
    for i in c:
        b = re.search(i, a)
        print "*"
        if b:
            b = b.group()
            break
    print b
    c = ['\d+元', '\d+息']
    for i in c:
        b = re.search(i, a)
        if b:
            b = b.group()
            break
    print b