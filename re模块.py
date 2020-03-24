#-*- coding:utf-8 -*- #
import re

if __name__ == '__main__':
    a = u"首付3000元起"
    b = re.search('\d+', a).group()
    print b
    c = [u'元', u'利息', u'息']
    for i in c:
        b = re.search(i, a).group()
        print "*"
        if b:
            break
    print b