#-*- coding:utf-8 -*- #
import random
import copy
import requests

class edge(object):
    def __init__(self, from_id, to_id, next_edge_id, is_required, weight = 1):
        self.from_id = from_id
        self.to_id = to_id
        self.weight = weight
        self.nxt = next_edge_id
        self.is_required = is_required

class node(object):
    def __init__(self, node_id, repeat_count = 1):
        self.repeat_count = repeat_count
        self.node_id = node_id

class connect_map(object):
    def __init__(self):
        self.head = [] #每个节点的第一条边序号
        self.tot = 0  #边的条数
        self.ed = [0] #存边的List
        self.nod = [] #节点的额外信息
    
    def init_node(self, node_num):
        for i in range(0, node_num + 1, 1): #0号节点作为最终起点
            self.nod.append(node(i))
            self.head.append(0)

    def addedge(self, from_id, to_id, is_required, weight = 1.0):
        self.tot += 1
        self.ed.append(edge(from_id, to_id, self.head[from_id], is_required, weight))
        self.head[from_id] = self.tot

def generate_idxs(cm, node_id, lst, end):
    #print lst
    edge_id = cm.head[node_id]
    candicates = {}
    rate_sum = 0.0
    while edge_id:
        if cm.nod[cm.ed[edge_id].to_id].repeat_count > 0:
            candicates[cm.ed[edge_id].to_id] = cm.ed[edge_id].weight
            rate_sum += cm.ed[edge_id].weight
        edge_id = cm.ed[edge_id].nxt
    
    while True:
        random_score = random.uniform(0,rate_sum)
        candicate = None
        for k,v in candicates.items():
            random_score -= v
            if random_score <= 0:
                candicate = k
                break
        if candicate != None:
            lst.append(candicate)
            cm.nod[candicate].repeat_count -= 1
            lst = generate_idxs(cm, candicate, lst, end)
            if lst[-1] != end:
                lst.pop()
                cm.nod[candicate].repeat_count += 1
            else:
                return lst
        else:
            return lst

def dfs(cm, node_id, lst):
    #print node_id
    edge_id = cm.head[node_id]
    lst.append(node_id)
    while edge_id > 0:
        dfs(cm, cm.ed[edge_id].to_id, lst)
        edge_id = cm.ed[edge_id].nxt
    return lst

if __name__ == '__main__':
    cm =connect_map()
    cm.init_node(10)
    cm.nod[3].repeat_count = 3
    cm.nod[6].repeat_count = 2
    cm.addedge(0,1,1)
    cm.addedge(1,2,1)
    cm.addedge(2,3,1)
    cm.addedge(3,3,1,0.3)
    cm.addedge(3,6,1,0.3)
    cm.addedge(6,3,1)
    cm.addedge(3,4,1,0.4)
    cm.addedge(4,5,1)
    bad_case = 0
    all_case = 0
    for i in range(10):
        am = copy.deepcopy(cm)
        lst = generate_idxs(am, 0, [], 5)
        all_case += 1
        print "{} : {}".format(all_case, lst)
        if lst[len(lst)-1] != 5:
            bad_case += 1
            print "{} : {}".format(bad_case, lst)
    print 1.0*bad_case/all_case