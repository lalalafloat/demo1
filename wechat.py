#-*- coding:utf-8 -*- #
import random
import copy
import requests
import itchat

def ldong():
    print('微信登入')
def edong():
    print('微信登出')
#登入
itchat.auto_login(hotReload=True,loginCallback=ldong, exitCallback=edong)