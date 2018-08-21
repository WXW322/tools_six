from netzob.all import *
from treelib import *
import numpy as np
import sys
import os
sys.path.append('../init_al')
sys.path.append('../deal_data')
sys.path.append('../protocol_analysis')
import session_deal
import ngramvec
import ngramentry
import ngramtree
import words_deal
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

    def test_iec(self,path,dire):
        t_srcs,t_des = self.read_diredatas(path)
        t_srcsdata = []
        t_desdata = []
        if dire == 0:
            for t_message in t_srcs:
                t_srcsdata.append(t_message.data)
        else:
            for t_message in t_des:
                t_srcsdata.append(t_message.data)
        ngram = ngramvec.ngramtree()
        standardout = sys.stdout
        if dire == 0:
            file = open('/home/wxw/paper/researchresult/iec104/source/VE_frestwocore.txt','w+')
        else:
            file = open('/home/wxw/paper/researchresult/iec104/destination/VE_frestwocore.txt', 'w+')
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
        print (t_entrys)
        ngram.get_idoms(t_fres)
        ngram.set_right([(0, 1), (1, 2), (2, 4), (4, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 12)])
        ngram.get_rightscore(ngram.rightidoms,ngram.idoms, 13)
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
        file = open('/home/wxw/paper/researchresult/iec104/VE_entryinfo.txt','w+')
        sys.stdout = file
        print(len(t_srcsdata))
        #for message in t_srcsdata:
        #    ngram.check_se(message[0:3])
        #sys.exit()
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()

        #ngram.print_htree()
        #ngram.check_childs('2_3_13')
        ngram.get_hnodes(2)

        #for t_message in t_srcsdata:
        #    data_p = t_message[6:9]
        #    ngram.find_sloentry(data_p)

        sys.stdout = standardout

    def test_iecbaseline(self,path,dire):
        t_srcs, t_des = self.read_diredatas(path)
        t_srcsdata = []
        t_desdata = []
        if dire == 0:
            for t_message in t_srcs:
                t_srcsdata.append(t_message.data)
        else:
            for t_message in t_des:
                t_srcsdata.append(t_message.data)
        ngram = ngramtree.ngramtree()
        standardout = sys.stdout
        if dire == 0:
            file = open('/home/wxw/paper/researchresult/iec104/source/VE_basetworight.txt', 'w+')
        else:
            file = open('/home/wxw/paper/researchresult/iec104/destination/VE_basetworight.txt', 'w+')
        sys.stdout = file
        print(len(t_srcsdata))
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()
        ngram.print_htree()
        ngram.get_conlos(t_srcsdata, 3)
        print(ngram.conlosfre)
        print(ngram.conlosentry)
        ngram.get_sumlos()
        ngram.baseline()
        baseline = ngram.get_idoms(ngram.baselinelos)
        print (baseline)
        ngram.set_right([(0,1),(1,2),(2,4),(4,6),(6,7),(7,8),(8,9),(9,10),(10,12)])
        ngram.get_rightscore(ngram.rightidoms,baseline,13)
        sys.stdout = standardout

    def test_modbusbaseline(self,path,dire):
        t_srcs, t_des = self.read_diredatas(path)
        t_srcsdata = []
        if dire == 0:
            for t_message in t_srcs:
                t_srcsdata.append(t_message.data)
        else:
            for t_message in t_des:
                t_srcsdata.append(t_message.data)

        ngram = ngramtree.ngramtree()
        standardout = sys.stdout
        file = open('/home/wxw/paper/researchresult/modbus/destination/VE_basetwor.txt', 'w+')
        sys.stdout = file
        print(len(t_srcsdata))
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()
        #print('aaa')
        #ngram.print_htree()
        ngram.print_htree()
        ngram.get_conlos(t_srcsdata, 3)
        print(ngram.conlosfre)
        print(ngram.conlosentry)
        ngram.get_sumlos()
        ngram.baseline()
        #print('bbb')
        baseline = ngram.get_idoms(ngram.baselinelos)
        print(baseline)
        ngram.set_right([(0,2),(2,4),(4,6),(6,7),(7,8)])
        ngram.get_rightscore(ngram.rightidoms,baseline, 9)
        sys.stdout = standardout

    def test_modbus(self, path,dire):
        t_srcs, t_des = self.read_diredatas(path)
        t_srcsdata = []
        t_desdata = []
        if dire == 0:
            for t_message in t_srcs:
                t_srcsdata.append(t_message.data)
        else:
            for t_message in t_des:
                t_srcsdata.append(t_message.data)
        ngram = ngramvec.ngramtree()
        standardout = sys.stdout
        file = open('/home/wxw/paper/researchresult/modbus/source/VE_frescore_final.txt', 'w+')
        sys.stdout = file
        print(len(t_srcsdata))
        # for message in t_srcsdata:
        #    ngram.check_se(message[0:3])
        # sys.exit()
        print("aaa")
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()
        print('bbb')
        # ngram.print_htree()
        ngram.get_conlos(t_srcsdata, 3)
        print(ngram.conlosfre)
        print(ngram.conlosentry)
        ngram.print_htree()
        t_fres, t_entrys = ngram.getlocationbyneibor(0.5 * len(t_srcsdata))
        print(t_fres)
        print(t_entrys)
        t_sumlos = ngram.merge_splits()
        print(t_sumlos)
        #ngram.get_idoms(t_fres)
        ngram.get_idoms(t_sumlos)
        ngram.set_right([(0,2),(2,4),(4,6),(6,7),(7,8)])
        ngram.get_rightscore(ngram.rightidoms, ngram.idoms, 9)
        sys.stdout = standardout
        # print (t_entrys)
        # print (ngram.get_idoms(t_entrys))

    def test_cipbaseline(self,path,dire):
        t_srcs, t_des = self.read_diredatas(path)
        t_srcsdata = []
        t_desdata = []
        if dire == 0:
            for t_message in t_srcs:
                t_srcsdata.append(t_message.data)
        else:
            for t_message in t_des:
                t_srcsdata.append(t_message.data)
        ngram = ngramtree.ngramtree()
        standardout = sys.stdout
        file = open('/home/wxw/paper/researchresult/cip/destination/VE_twobase.txt', 'w+')
        sys.stdout = file
        print(len(t_srcsdata))
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()
        ngram.print_htree()
        ngram.get_conlos(t_srcsdata, 3)
        print(ngram.conlosfre)
        print(ngram.conlosentry)
        ngram.get_sumlos()
        ngram.baseline()
        baseline = ngram.get_idoms(ngram.baselinelos)
        print(baseline)
        ngram.set_right([(0,2),(2,4),(4,8),(8,12),(12,20),(20,24)])
        ngram.get_rightscore(baseline, ngram.rightidoms, 25)
        sys.stdout = standardout

    def test_cip(self,path,dire):
        t_srcs, t_des = self.read_diredatas(path)
        t_srcsdata = []
        t_desdata = []
        if dire == 0:
            for t_message in t_srcs:
                t_srcsdata.append(t_message.data)
        else:
            for t_message in t_des:
                t_srcsdata.append(t_message.data)
        ngram = ngramvec.ngramtree()
        standardout = sys.stdout
        file = open('/home/wxw/paper/researchresult/cip/VE_twovecsocre.txt', 'w+')
        sys.stdout = file
        print(len(t_srcsdata))
        ngram.build_tree(t_srcsdata, 3)
        ngram.caculate_prob()
        # ngram.print_htree()
        ngram.get_conlos(t_srcsdata, 3)
        print(ngram.conlosfre)
        print(ngram.conlosentry)
        t_fres, t_entrys = ngram.getlocationbyneibor(0.5 * len(t_srcsdata))
        print(t_fres)
        ngram.get_idoms(t_fres)
        ngram.set_right([(0, 2), (2, 4), (4, 8), (8, 12), (12, 20), (20, 24)])
        ngram.get_rightscore(ngram.rightidoms, ngram.idoms, 25)
        sys.stdout = standardout

    def get_loinfo(self,datas,location,info_dir):
        l_s = location[0]
        l_e = location[1]
        location_f = words_deal.message_dealer(datas)
        standardout = sys.stdout
        file = open(info_dir, 'w+')
        sys.stdout = file
        if (location_f.find_constone(l_s,l_e) == 1):
            return 1
        elif(location_f.find_lenbyaccu(datas,l_s,l_e) == 1):
            return 2
        sys.stdout = standardout








starttime = time.time()
exp = exforresults()
#exp.test_cipbaseline('/home/wxw/data/cip_test',1)
#exp.test_iecbaseline('/home/wxw/data/iec104',1)
#exp.test_modbusbaseline('/home/wxw/data/modbusdata')
#exp.test_cip('/home/wxw/data/cip_test')
#exp.find_sevenr('//home/wxw/data/iec104')
exp.test_modbus('/home/wxw/data/modbusdata',0)
#exp.test_iec('/home/wxw/data/iec104',1)
#src,des = exp.read_diredatas('/home/wxw/data/iec104')
#print(exp.get_loinfo(src,(2,4),'/home/wxw/paper/researchresult/iec104/lo_info/nonlength_info'))
endtime = time.time()
print('Running time: %s Seconds'%(endtime-starttime))

