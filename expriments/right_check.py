from netzob.all import *
from treelib import *
import numpy as np
import sys
import os
sys.path.append('../init_al')
sys.path.append('../deal_data')
import session_deal
import ngramvec
import ngramentry
import ngramtree
import time


def get_rightr():
    t_r = {}
    t_r[2] = 3
    t_r[1] = 3
    t_r[3] = 2
    t_r[4] = 2
    t_sum = 0
    t_num = []
    for key in t_r:
        t_sum = t_sum + t_r[key]
    for key in t_r:
        t_r[key] = -np.log(t_r[key]/t_sum)
        t_num.append(t_r[key])
    t_num = np.array(t_num)
    t_mean = np.mean(t_num)
    std = np.std(t_num,ddof=1)
    for key in t_r:
        t_r[key] = (t_r[key] - t_mean) / std
    print(t_r)

#t_datas = PCAPImporter.readFile('/home/wxw/data/modbusdata/141.81.0.10141.81.0.24.pcap').values()
#print (type(t_datas[0].data))

b = (14537).to_bytes(4,byteorder='big')
print('r is %s'%(b))

"""
ngram = ngramtree.ngramtree()
ngram.build_tree([[1,1,2,1,3,2,3,4,4,2]], 3)
ngram.caculate_prob()
ngram.print_htree()
get_rightr()
"""
