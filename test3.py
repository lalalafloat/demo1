#-*- coding:utf-8 -*- #
#求100以内素数 傻逼版
def get_prime_list(up):
    lst = []
    for i in range(2, up, 1):
        flag = 0
        for j in range(2, i, 1):
            if i%j == 0:
                flag = 1
                break
            if j*j == i:
                break
        if flag == 0:
            lst.append(i)
    return lst

def subseqs(s):
    if len(s)==1:
        return [s]
    else:
        s1 = subseqs(s[:1])
        s2 = subseqs(s[1:])
        #print s1,s2
        s = s1 + s2
        if [] not in s:
            s.append([])
        for i in s1:
            for j in s2:
                if i+j not in s:
                    s.append(i+j)
        return s
                

if __name__ == '__main__':
    #print get_prime_list(100)
    a = [1,2,3,4]
    b = [5,6]
    print cross(a,b)
    print subseqs(a)