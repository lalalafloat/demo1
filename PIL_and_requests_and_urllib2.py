#-*- coding:utf-8 -*- #
import urllib2
import requests
from PIL import Image, ImageFilter
import io

if __name__ == '__main__':
    img = 'http://www.baidu.com/img/baidu_jgylogo3.gif'
    file1 = urllib2.urlopen(img, timeout = 2).read() #直接返回图片数据
    #print file1
    file2 = requests.get(img, timeout = 2) #返回HTTP响应类  resp.content才是数据
    #print file2.status_code, file2.content
    #print Image.open(io.BytesIO(file2))
    im = Image.open(file2)
    print im.size
