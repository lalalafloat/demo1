#branch car from car
#branch master
#branch car2
#branch master2 self
#branch car2
#branch car2 not commit
#another test 5/11
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
    print"test git branch"
