from netzob.all import *
import os
import time
import sys

def read_data(dir):
    paths = os.listdir(dir)
    t_datas = []
    t_sedatas = []
    for path in paths:
        t_path = os.path.join(dir, path)
        t_data = PCAPImporter.readFile(t_path).values()
        t_datas.extend(t_data)
    for t_data in t_datas:
        t_sedatas.append(t_data.data)
    return t_sedatas

def clus_bynw(datas,value):
    pre_messages = []
    for data in datas:
        t_data = RawMessage(data)
        pre_messages.append(t_data)
    f_clus = Format()
    t_r = f_clus.clusterByAlignment(messages = pre_messages,minEquivalence = value)
    return t_r



def get_tcount(clus,lo):
    t_s = lo[0]
    t_e = lo[1]
    t_n = {}
    for clu in clus:
        if(len(clu) < t_e + 1):
            t_id = clu[2]
            t_temp = 3&t_id
            if t_temp == 3:
                t_n['uu'] = 1
            else:
                t_n['ss'] = 1
        t_key = clu[t_s:t_e]
        if t_key not in t_n:
            t_n[t_key] = 1
    return len(t_n)

def split_byfc(messages,t_lo):
    t_s = t_lo[0]
    t_e = t_lo[1]
    t_fme = {}
    
    for message in messages:
        if len(message) < t_e + 1:
            t_id = int.from_bytes(message[2:3],byteorder="big")
            t_temp = t_id&3
            if t_temp == 3:
                if 'uu' not in t_fme:
                    t_fme['uu'] = []
                t_fme['uu'].append(message)
            else:
                if 's' not in t_fme:
                    t_fme['ss'] = []
                t_fme['ss'].append(message)
            continue
        t_key = message[t_s:t_e]
        if t_key not in t_fme:
            t_fme[t_key] = []
        t_fme[t_key].append(message)
    return t_fme

def sample_data(messages,T):
    t_count = len(messages)
    t_avg = T/t_count
    i = 0
    t_f = []
    t_sum = 0
    t_ps = {}
    for key in messages:
        if(len(messages[key]) < t_avg):
            t_f.extend(messages[key])
            t_sum = t_sum + len(messages[key])
            t_ps[key] = 0
    left_c = t_count - len(t_ps)
    left_l = T - t_sum
    left_avn = left_l / left_c
    for key in messages:
        if(key not in t_ps):
            t_f.extend(messages[key][0:int(left_avn)])
        i = i + 1
    return t_f

def get_keyclus(clus,key,r_lo):
    t_c = 0
    for clu in clus:
        t_lo = 0
        if key == 'uu':
            for idom in clu:

                t_id = int.from_bytes(idom[2:3],byteorder="big")
                t_temp = 3&t_id
                if(t_temp == 3):
                    t_lo = 1
                    break
        elif key == 'ss':
            for idom in clu:
                t_id = int.from_bytes(idom[2:3],byteorder="big")
                t_temp = 3&t_id
                if(t_temp == 1):
                    t_lo = 1
                    break
        else:
            for idom in clu:
                if(len(idom) > r_lo[1] + 1 and idom[r_lo[0]:idom[r_lo[1]]] == key):
                    t_lo = 1
                    break
        if(t_lo == 1):
            t_c = t_c + 1
    return t_c

def get_precess(clus,r_lo,keys):
    t_r = 0
    t_pre = 0
    for clu in clus:
        t_cu = get_tcount(clu,r_lo)
        if t_cu == 1:
            t_r = t_r + 1
    for key in keys:
        if(key == 'ss'):
            t_cu = get_keyclus(clus,key,(2,3))
        elif(key == 'uu'):
            t_cu = get_keyclus(clus,key,(2,3))
        else:
            t_cu = get_keyclus(clus,key,r_lo)
        if t_cu == 1:
            t_pre = t_pre + 1
    print(t_r,t_pre,t_r/len(clus),t_pre/len(keys))
    return(t_r,t_pre,t_r/len(clus),t_cu/len(keys))

def print_binary(datas):
    for data in datas:
        print(data,end=' ')
    print()

def print_clus(datas,args):
    print(args + 'start:')
    if(len(datas) < 1):
        return
    else:
        for data in datas:
            print_binary(data)
    print(args + 'end:')
    print()

def get_results(s_path,des_path,los,para):
    t_output = sys.stdout
    file = open(des_path,'w+')
    sys.stdout = file
    datas = read_data(s_path)
    t_funclus = split_byfc(datas,los)
    #print('split_start')
    #for t_key in t_funclus:
    #    print_clus(t_funclus[t_key],'p')
    #print('split_end')

    t_fdatas = sample_data(t_funclus,2000)
    #print_clus(t_fdatas,'sample')
    t_clus = clus_bynw(t_fdatas,para)
    t_fmes = []
    for t_clu in t_clus:
        t_messages = t_clu.messages
        t_M = []
        for t_me in t_messages:
            t_M.append(t_me.data)
        t_fmes.append(t_M)

        #print_clus(t_M,'nw')


    get_precess(t_fmes,los,t_funclus.keys())












starttime = time.time()
#data = read_data('/home/wxw/data/modbustest')
#clus_bynw(data)
#for i in [80,70,60,50,40,30,20,10]:
#    get_results('/home/wxw/data/modbustest','/home/wxw/paper/researchresult/classify/modbus/netzob/out'+str(i),(7,8),i)
get_results('/home/wxw/data/iec104','/home/wxw/paper/researchresult/classify/iec104/netzob/out_t'+str(40),(6,7),40)
endtime = time.time()
print("time is:",endtime - starttime)