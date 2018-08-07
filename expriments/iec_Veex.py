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

class exforresults:
    def __init__(self):
        self.sessiondeal = session_deal.session_deal('')


    def read_diredata(self,filename):
        data = PCAPImporter.readFile(filename).values()
        srcdata,desdata = self.sessiondeal.clus_sesionbydi(data)
        return srcdata,desdata

    def read_diredatas(self,path):
        files = os.listdir(path)
        src_datas = []
        des_datas = []
        for file in files:
            filepath = os.path.join(path,file)
            t_src,t_des = self.read_diredata(filepath)
            src_datas.extend(t_src)
            des_datas.extend(t_des)
        return src_datas,des_datas

    def test_iec(self,path):
        t_srcs,t_des = self.read_diredatas(path)
        t_srcsdata = []
        t_desdata = []
        for t_message in t_srcs:
            t_srcsdata.append(t_message.data)
        ngram = ngramvec.ngramtree()
        standardout = sys.stdout
        file = open('/home/wxw/paper/researchresult/iec104/VE_frescore.txt','w+')
        sys.stdout = file
        print(len(t_srcsdata))
        #for message in t_srcsdata:
        #    ngram.check_se(message[0:3])
        #sys.exit()
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()
        #ngram.print_htree()
        ngram.get_conlos(t_srcsdata, 3)
        print (ngram.conlosfre)
        print (ngram.conlosentry)
        t_fres, t_entrys = ngram.getlocationbyneibor(0.5 * len(t_srcsdata))
        print(t_fres)
        ngram.get_idoms(t_fres)
        ngram.set_right([(0, 1), (1, 2), (2, 4), (4, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 12)])
        ngram.get_rightscore(ngram.idoms, ngram.rightidoms, 13)
        #print (t_entrys)
        #print (ngram.get_idoms(t_entrys))

        sys.stdout = standardout

    def find_sevenr(self,path):
        t_srcs,t_des = self.read_diredatas(path)
        t_srcsdata = []
        t_desdata = []
        for t_message in t_srcs:
            t_srcsdata.append(t_message.data)
        ngram = ngramentry.ngramtree()
        standardout = sys.stdout
        file = open('/home/wxw/paper/researchresult/iec104/VE_counttree.txt','w+')
        sys.stdout = file
        print(len(t_srcsdata))
        #for message in t_srcsdata:
        #    ngram.check_se(message[0:3])
        #sys.exit()
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()

        ngram.print_htree()
        ngram.check_childs('2_3_13')

        #for t_message in t_srcsdata:
        #    data_p = t_message[6:9]
        #    ngram.find_sloentry(data_p)

        sys.stdout = standardout

    def test_iecbaseline(self,path):
        t_srcs, t_des = self.read_diredatas(path)
        t_srcsdata = []
        t_desdata = []
        for t_message in t_srcs:
            t_srcsdata.append(t_message.data)
        ngram = ngramtree.ngramtree()
        standardout = sys.stdout
        file = open('/home/wxw/paper/researchresult/iec104/VE_base.txt', 'w+')
        sys.stdout = file
        print(len(t_srcsdata))
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()
        ngram.print_htree()
        ngram.get_conlos(t_srcsdata, 3)
        ngram.get_sumlos()
        ngram.baseline()
        baseline = ngram.get_idoms(ngram.baselinelos)
        print (baseline)
        ngram.set_right([(0,1),(1,2),(2,4),(4,6),(6,7),(7,8),(8,9),(9,10),(10,12)])
        ngram.get_rightscore(baseline,ngram.rightidoms,13)
        sys.stdout = standardout


starttime = time.time()
exp = exforresults()
exp.test_iec('/home/wxw/data/iec104')
endtime = time.time()
print('Running time: %s Seconds'%(endtime-starttime))

