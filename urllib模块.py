#-*- coding:utf-8 -*- #
import urllib2
import requests
import json

if __name__ == '__main__':
    img = 'http://www.baidu.com/img/baidu_jgylogo3.gif'
    file = urllib2.urlopen(img, timeout = 2).read()
    print file
    #file = requests.get(img, timeout = 2)
    #print file.status_code, file.content