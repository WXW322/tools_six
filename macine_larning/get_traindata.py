
import pandas as pd
import numpy as np
from netzob.all import *
import struct
import sys
sys.path.append('../classify_6/frequent_find')
import series_find
import find_one

class produce_medata:
    def __init__(self,datas):
        self.onelable = {}
        self.datas = datas

    def get_lable(self,datas,lo_s):
        t_r = {}
        t_lable = []
        t_value = []
        t_lo = []
        for data in datas:
            t_length = len(data.data)
            i = 0
            while(i < t_length):
                t_lo.append(i)
                t_node = str(data.data[i:i+1])
                t_node = struct.unpack('>B',t_node)
                t_value.append(t_node[0])
                if i in lo_s:
                    t_lable.append(1)
                else:
                    t_lable.append(0)
                i = i + 1
        t_r['value'] = t_value
        t_r['lo'] = t_lo
        t_r['lable'] = t_lable
        self.onelable = t_r
        g_r = pd.DataFrame(t_r)
        g_r.to_csv('/home/wxw/data/iec104_train/lable_total.csv',index=None)

    def get_loinfo(self):
        l_feature = find_one.frequents_find(self.datas)
        t_f = l_feature.get_detaillo(10000)
        t_info = {}
        t_tran = np.array(t_f).T
        t_info['lo'] = t_tran[0]
        t_info['num'] = t_tran[1]
        t_info['total_rate'] = t_tran[2]
        t_info['num_max'] = t_tran[3]
        t_info['num_min'] = t_tran[4]
        t_info['mean'] = t_tran[5]
        t_info['gap'] = t_tran[6]
        t_info['middle'] = t_tran[7]
        t_info['var'] = t_tran[8]
        lo_info = pd.DataFrame(t_info)
        return lo_info

    def data_combine(self,data_one,data_two,key):
        data_new = data_one.merge(data_two,on = 'lo')
        data_new.to_csv('/home/wxw/data/iec104_train/lable_finalone.csv',index=None)



def get_train():
    data = PCAPImporter.readFile('/home/wxw/data/iec104/10.55.37.310.55.218.2.pcap').values()
    dd = produce_medata(data)
    t_R = dd.get_loinfo()
    dd.get_lable(data,[0,6,8])
    tt = pd.read_csv('/home/wxw/data/iec104_train/lable_total.csv')
    t_f = dd.data_combine(t_R,tt,'lo')


get_train()