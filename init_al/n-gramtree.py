from netzob.all import *
from treelib import *
import numpy as np
import sys

class ngramtree:
    def __init__(self):
        self.tree = Tree()
        self.tree.create_node(tag = '0_0',identifier = '0_0',data = [0])

    def tract(self,name):
        los = name.split('_')
        return los

    def addnode(self,p_name,n_num,depth):
        name = str(depth) + '_' + str(n_num) + '_' + self.tract(p_name)[1]
        if(self.tree.contains(name)):
            t_node = self.tree.get_node(name)
            t_node.data[0] = t_node.data[0] + 1
        else:
            self.tree.create_node(tag = name,identifier = name,data = [1],parent = p_name)
        return name

    def add_sequence(self,sequence):
        t_len = len(sequence)
        i = 0
        while(i < t_len):
            if i == 0:
                p_name = '0_0'
            t_num = sequence[i]
            p_name = self.addnode(p_name,t_num,i + 1)
            i = i + 1


    def build_tree(self,sequences,L):
        for sequence in sequences:
            t_len = len(sequence)
            i = 0
            while(i < t_len):
                if i <= t_len - L:
                    self.add_sequence(sequence[i:i+L])
                else:
                    self.add_sequence(sequence[i:])
                i = i + 1

    def print_tree(self):
        for node in self.tree.all_nodes():
            print (node.identifier + '  ' + str(node.data))

    def get_h(self,h):
        t_nodes = []
        for node in self.tree.all_nodes():
            if int(self.tract(node.identifier)[0]) == h:
                t_nodes.append(node.identifier)
        return t_nodes


    def caculate_prob(self):
        t_H = self.tree.depth()
        t_h = 1
        while(t_h <= t_H):
            t_hnodes = self.get_h(t_h)
            t_sum = 0
            t_hpro = []
            t_cpro = []
            for t_n in t_hnodes:
                t_sum = self.tree.get_node(t_n).data[0] + t_sum
                t_node = self.tree.get_node(t_n)
                if t_node.is_leaf():
                    t_node.data.append(0)
                    continue
                t_childrens = self.tree.children(t_n)
                t_shang = 0
                for child in t_childrens:
                    t_shang = t_shang + (child.data[0]/t_node.data[0])*np.log(child.data[0]/t_node.data[0])
                t_node.data.append(-t_shang)
            for t_n in t_hnodes:
                t_node = self.tree.get_node(t_n)
                t_node.data.append(t_node.data[0] / t_sum)
                t_hpro.append(t_node.data[0]/t_sum)
                t_cpro.append(t_node.data[1])
            print (t_h)
            print (t_hpro)
            t_ndata = np.array(t_hpro)
            mean = np.mean(t_ndata)
            std = np.std(t_ndata,ddof=1)
            t_sdata = np.array(t_cpro)
            mean_s = np.mean(t_sdata)
            std_s = np.std(t_sdata,ddof=1)
            for t_n in t_hnodes:
                t_node = self.tree.get_node(t_n)
                if(std != 0):
                    t_node.data[2] = (t_node.data[2] - mean)/std
                else:
                    t_node.data[2] = (t_node.data[2] - mean)
                if(mean_s == 0 and std_s ==0):
                    continue
                t_node.data[1] = (t_node.data[1] - mean_s)/std_s
            t_h = t_h + 1

    def find_slo(self,aa):
        print ('111')













ngram = ngramtree()
ngram.build_tree(['aabbaacdee'],3)
ngram.caculate_prob()
ngram.print_tree()

