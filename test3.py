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

if __name__ == '__main__':
    print get_prime_list(100)