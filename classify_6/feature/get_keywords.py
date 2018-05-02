
from netzob.all import *
import pandas as pd

def get_unique(filename,lo):
    messages = PCAPImporter.readFile(filename).values()
    t_list = []
    for me in messages:
        t_c = me.data[7]
        if t_c not in t_list:
            t_list.append(t_c)
    print len(t_list)


#get_unique('/home/wxw/data/iec_right.pcap',)

cc = pd.DataFrame()
bb = cc.sample(frac = 0.1)