#-*- coding:utf-8 -*- #
import random

class edge(object):
    def __init__(self, from_id, to_id, next_edge_id,  weight = 1):
        self.from_id = from_id
        self.to_id = to_id
        self.weight = weight
        self.nxt = next_edge_id

class node(object):
    def __init__(self, node_id, repeat_count = 0):
        self.repeat_count = repeat_count
        self.node_id = node_id

class connect_map(object):
    def __init__(self):
        self.head = [0] #每个节点的第一条边序号
        self.tot = 0  #边的条数
        self.ed = [0] #存边的List
        self.nod = [0] #节点的额外信息
    
    def init_node(self, node_num):
        for i in range(1, node_num + 1, 1):
            self.nod.append(node(0,i))
            self.head.append(0)

    def addedge(self, from_id, to_id, weight = 1.0):
        self.tot += 1
        self.ed.append(edge(from_id, to_id, weight, self.head[from_id]))
        self.head[from_id] = self.tot

def dfs(cm, node_id, lst):
    print node_id
    edge_id = cm.head[node_id]
    lst.append(node_id)
    while edge_id:
        dfs(cm, cm.ed[edge_id].to_id, lst)
        edge_id = cm.ed[edge_id].nxt
    return lst

if __name__ == '__main__':
    cm =connect_map()
    cm.init_node(10)
    cm.addedge(1,2)
    cm.addedge(2,3)
    cm.addedge(3,4)
    lst = []
    print dfs(cm, 1, lst)