#-*- coding:utf-8 -*- #
import random
import copy
import requests

class edge(object):
    def __init__(self, from_id, to_id, next_edge_id, weight = 1):
        self.from_id = from_id
        self.to_id = to_id
        self.weight = weight
        self.nxt = next_edge_id

class node(object):
    def __init__(self, node_id, repeat_count = 1):
        self.repeat_count = repeat_count
        self.node_id = node_id
        self.depth = 0
        self.choice = 0

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

    def addedge(self, from_id, to_id, weight = 1.0):
        self.tot += 1
        self.ed.append(edge(from_id, to_id, self.head[from_id], weight))
        self.head[from_id] = self.tot

def bfs_map(cm, st_node):
    queue = [st_node]
    while len(queue):
        now_node = queue.pop(0)
        depth = now_node.depth
        now_node_id = now_node.node_id
        #print "node_id = {}     depth = {}".format(now_node_id,depth)
        edge_id = cm.head[now_node_id]
        while edge_id:
            #print "edge_id = {}".format(edge_id)
            to_node_id = cm.ed[edge_id].to_id
            if cm.nod[to_node_id].depth == 0:
                cm.nod[to_node_id].depth = depth + 1
                queue.append(cm.nod[to_node_id])
            edge_id = cm.ed[edge_id].nxt

def generate_idxs(cm, node_id, lst):
    #print lst
    edge_id = cm.head[node_id]
    same_candicates = {}
    deeper_candicates = {}
    candicates = {}
    same_rate_sum = 0.0
    deeper_rate_sum = 0.0
    rate_sum = 0.0
    while edge_id:
        if cm.nod[cm.ed[edge_id].to_id].repeat_count > 0:
            deeper_candicates[cm.ed[edge_id].to_id] = cm.ed[edge_id].weight
            deeper_rate_sum += cm.ed[edge_id].weight
            if cm.nod[cm.ed[edge_id].to_id].depth == cm.nod[node_id].depth and cm.nod[cm.ed[edge_id].to_id].choice == 0:
                same_candicates[cm.ed[edge_id].to_id] = cm.ed[edge_id].weight
                same_rate_sum += cm.ed[edge_id].weight
        edge_id = cm.ed[edge_id].nxt
    if same_candicates:
        candicates = same_candicates
        rate_sum = same_rate_sum
    else:
        candicates = deeper_candicates
        rate_sum = deeper_rate_sum
    random_score = random.uniform(0,rate_sum)
    candicate = None
    for k,v in candicates.items():
        random_score -= v
        if random_score <= 0:
            candicate = k
            break
    if candicate != None:
        cm.nod[candicate].choice = 1
        lst.append(candicate)
        cm.nod[candicate].repeat_count -= 1
        return generate_idxs(cm, candicate, lst)
    else:
        return lst


if __name__ == '__main__':
    cm =connect_map()
    cm.init_node(10)
    cm.nod[3].repeat_count = 3
    cm.nod[6].repeat_count = 2
    cm.addedge(0,1)
    cm.addedge(1,2)
    cm.addedge(2,3)
    cm.addedge(2,6)
    cm.addedge(3,3)
    cm.addedge(3,6)
    cm.addedge(6,3)
    cm.addedge(3,4)
    cm.addedge(6,4)
    cm.addedge(4,5)
    bad_case = 0
    all_case = 0
    bfs_map(cm, cm.nod[0])
    for i in cm.nod:
        print "{}   :   {}".format(i.node_id, i.depth)
    print generate_idxs(cm, 0, [])
    '''
    for i in range(10):
        am = copy.deepcopy(cm)
        lst = generate_idxs(am, 0, [], 5)
        all_case += 1
        #print "{} : {}".format(all_case, lst)
        if lst[len(lst)-1] != 5:
            bad_case += 1
            print "{} : {}".format(bad_case, lst)
    print 1.0*bad_case/all_case
    '''