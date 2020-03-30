#-*- coding:utf-8 -*- #
import re

if __name__ == '__main__':
    a = u"首付3000起"
    b = re.search('\d+', a).group()
    print b
    c = [u'元', u'利息', u'息']
    for i in c:
        b = re.search(i, a)
        print "*"
        if b:
            b = b.group()
            break
    print b