#-*- coding:utf-8 -*- #  
from enum import Enum
class data(Enum):
    Name = 1
    Class = 2
    Grade = 3

if __name__ == '__main__':
    print "data.Name.value = {}".format(data.Name.value)