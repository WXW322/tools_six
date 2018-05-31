from netzob.all import *
from treelib import *
import sys

class fre_tree:
    def __init__(self):
        self.trees = None
        self.modes = []

    def get_right(self,nods,dep):
        pn = []
        for nod in nods:
            if int(nod.identifier[1]) == dep:
                pn.append(nod.identifier)
        return pn
    def creat_session(self,depth):
        tt = Tree()
        tt.create_node(tag = 'n00', identifier = 'n00' ,data = 0)
        i = 1
        while(i <= depth):
            j = 1
            while( j <= 4):
                t_name = 'n' + str(i) + str(j)
                t_parents = self.get_right(tt.all_nodes(),i-1)
                m = 0
                for t_pa in t_parents:
                    tt.create_node(tag = t_name + str(m),identifier = t_name + str(m),data = 0,parent = t_pa)
                    m = m + 1
                j = j + 1
            i = i + 1
        self.trees = tt
    def update_num(self,t_series):
        t_len = len(t_series)
        i = 0
        t_ctree = self.trees.subtree('n00')
        while(i < t_len):
            t_data = t_series[i]
            t_id = 'n' + str(i + 1) + str(t_data)
            t_condidates = t_ctree.children(t_ctree.root)
            for con in t_condidates:
                if(con.tag[0:3] == t_id):
                    self.trees[con.tag].data = self.trees[con.tag].data + 1
                    t_ctree = t_ctree.subtree(con.tag)
                    break
            i = i + 1

    def find_fre(self,rate,s_leng,t_len):
        while(t_len >= 1):
            t_bound = (s_leng / t_len) * rate
            t_nodes = self.get_right(self.trees.all_nodes(),t_len)
            for t_n in t_nodes:
                if (self.trees.get_node(t_n).data < t_bound):
                    t_lo = 0
                    for t_con in self.trees.children(t_n):
                        if t_con.tag == 'right':
                            t_lo = 1
                            break
                    if(t_lo == 0):
                        self.trees.remove_node(t_n)
                    else:
                        self.trees.get_node(t_n).tag = 'right'
                else:
                    self.trees.get_node(t_n).tag = 'right'
            t_len = t_len - 1
    def depth_traverse(self,identy,t_s):
        t_node = self.trees.get_node(identy)
        if(t_node.is_leaf()):
            t_s = t_s + t_node.identifier[2]
            self.modes.append(t_s)
        else:
            t_lags = self.trees.children(identy)
            t_s = t_s + t_node.identifier[2]
            for tg in t_lags:
                self.depth_traverse(tg.identifier,t_s)



    def get_sessionmode(self):
        temp_nodes = self.trees.children('n00')
        for t_no in temp_nodes:
            self.depth_traverse(t_no.identifier,'')

    def get_idom(self):
        print ('aa')






ff = fre_tree()
ff.creat_session(4)
s_l = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]
i = 4
while(i < len(s_l) - 1):
    ff.update_num(s_l[i-4:i])
    i = i + 1
ff.find_fre(0.5,10,4)
ff.get_sessionmode()
for s in ff.modes:
    print (s)















