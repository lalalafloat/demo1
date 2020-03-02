import logging
import sys
def sorted(a):
    logging.info("a = {}".format(a))
    a.sort()    
    return a

if __name__ == '__main__':
    a = [1,5,2,3]
    print sorted(a)
    x = []
    print sys.getrefcount(x)
    y = x
    z = y
    print sys.getrefcount(x)
    x = 1 
    print sys.getrefcount(x)