#-*- coding:utf-8 -*- #

import random

def get_count(pattern, module):
    lenn = len(pattern)
    cont = 0
    for i in range(lenn-1, len(module), 1):
        flag = 0
        for j in range(lenn):
            if pattern[j] != module[i-lenn+1+j]:
                flag = 1
                break
        if flag == 0:
            cont += 1
    return cont

def get_template_sequence(lst, lenn):
    seq = [0]
    candi = []
    for i in range(len(lst)):
        candi.extend(lst[i])
        lst[i] = [0] + lst[i]
    #print lst
    candi = list(set(candi))
    probability = {}
    while True:
        up = min(len(seq), lenn)
        #print "---- up = {}".format(up)
        for cad in candi:
            prob = 1.0
            for i in range(1, up + 1, 1):
                #print "up = {}".format(up)
                pre, now = 0, 0
                for ls in lst: #匹配
                    pre += get_count(seq[len(seq)-i:], ls)
                    now += get_count(seq[len(seq)-i:]+[cad], ls)
                #print "{} : {}     {} : {}".format(seq[len(seq)-i:], pre, seq[len(seq)-i:]+[cad], now)
                rate = 0.0
                if pre>0:
                    rate = 1.0*now/pre
                prob *= rate
            probability[cad] = prob
        #print probability
        candicates = []
        sum_prob = 0.0
        for k,v in probability.items():
            if v > 0:
                candicates.append((k,v))
                sum_prob += v
        if len(candicates) == 0:
            break
        great = random.uniform(0,sum_prob)
        for candicate in candicates:
            great -= candicate[1]
            if great <= 0:
                seq.append(candicate[0])
                break
        #print "seq = {}".format(seq)
    return seq[1:]
                    

if __name__ == '__main__':
    '''
    lst = []
    lst.append([1, 3, 5, 4, 10, 6, 10, 10, 12, 7, 8, 9, 11])
    lst.append([1,4,3,5,10,6,10,10,12,7,8,9,11])
    lst.append([4,3,5,10,6,10,10,12,7,8,9,11])
    lst.append([3,5,1,4,6,10,10,10,7,8,9,11])
    lst.append([4,3,5,2,1,10,10,10,7,8,9])
    '''
    lst = [
        [3,6,8,9,10,11,5],
        [1,2,6,8,7,10,11,5],
        [3,6,7,8,9,10,5],
        [3,6,7,8,10,11,5],
        [3,6,8,9,10,11,5],
        [1,2,6,7,8,9,10,5],
        [1,2,6,8,9,7,10,5],
    ]
    a = [1,2,3]
    #print a[1:]
    b = [1,2,3,5,6,1,2,3]
    #print get_count(a,b)
    seq = get_template_sequence(lst,1)
    print seq
    flag = 0
    for ls in lst:
        if cmp(ls,seq):
            flag = 1
            break
    if flag == 0:
        print "false"
    else:
        print "true"
