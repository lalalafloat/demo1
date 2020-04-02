#-*- coding:utf-8 -*- #

#import Tkinter as tk
#import tkFont

 

 
'''
def display_font(text, font_family, font_size):

   root = tk.Tk()

   canvas = tk.Canvas(root, width=200, height=100)

   canvas.pack()

   (x,y) = (5,5)

   pttopx = lambda x:int(x * 3 // 4)

   font_size=pttopx(font_size)

   font = tkFont.Font(family=font_family, size=font_size)

   w= font.measure(text)

   h= font.metrics("linespace")

   print "Font Family is %s, Font Size is %d pt" % (font_family,font_size)

   print "Text Width is %s px, height is %s px" % (w,h)

   canvas.create_text(x,y,text=text,font=font,anchor=tk.NW)

   tk.mainloop()
'''

def get_text_length(text, font_size):
    pass

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
 
def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar<=u'\u0039':
       return True
    else:
       return False
 
def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False

if __name__ == '__main__':
    #display_font("Paramètres de recherc","tahoma",11)
    a = "奥迪as3dA4"
    a = a.decode('utf-8')
    for i in a:
        if is_chinese(i):
            print "中文"
        elif is_alphabet(i):
            print "英文"
        elif is_number(i):
            print "数字"