#coding=utf-8
from netzob.all import *
import struct
import math
import os
import sys
import words_basic

class message_dealer:
    def __init__(self,messages):
        self.messages = messages
        self.const = []

    def find_const(self):
        #develop absolute or relative
        conster = words_basic.words_base()
        t_messages = []
        for message in self.messages:
            t_messages.append(message.data)
        t_r,t_l = conster.get_loinfo(t_messages,20)
        t_tol = len(self.messages)
        i = 0
        t_len = len(t_r)
        while(i < t_len):
            t_idom = t_r[i]
            t_max = t_idom[0][1]
            if(t_max / t_tol >= 0.95):
                self.const.append(i)
            i = i + 1

    def find_senum(self,Mone,Mtwo,gap,leixing,encoding):
        # delevepe effective add direction
        length_one = len(Mone.data)
        length_two = len(Mtwo.data)
        #print (Mone)
        #print (Mtwo)
        #sys.exit()
        t_length = min(length_one,length_two)
        i = 0
        t_condilo = []
        while(i < t_length - gap):
            if(i in self.const):
                i = i + 1
                continue
            j = 0
            while(j < t_length - gap):
                if(j in self.const):
                    j = j + 1
                    continue
                t_strone = struct.unpack(encoding + leixing,Mone.data[i:i+gap+1])[0]
                t_strtwo = struct.unpack(encoding + leixing,Mtwo.data[j:j+gap+1])[0]
                #print(i,j)
                #print(Mone.data[i:i+gap+1])
                #print(Mtwo.data[j:j+gap+1])
                #print(t_strone)
                #print(t_strtwo)
                if(t_strone == t_strtwo):
                    t_condilo.append((i,j))
                j = j + 1
            i = i + 1

        return t_condilo

    def find_senumsub(self,Mone,Mtwo,gap,leixing,encoding):
        # delevepe effective add direction
        length_one = len(Mone.data)
        length_two = len(Mtwo.data)
        #print (Mone)
        #print (Mtwo)
        #sys.exit()
        t_length = min(length_one,length_two)
        i = 0
        t_condilo = []
        while(i < t_length - gap):
            if(i in self.const):
                i = i + 1
                continue
            j = 0
            while(j < t_length - gap):
                if(j in self.const):
                    j = j + 1
                    continue
                t_strone = struct.unpack(encoding + leixing,Mone.data[i:i+gap+1])[0]
                t_strtwo = struct.unpack(encoding + leixing,Mtwo.data[j:j+gap+1])[0]
                print(i,j)
                print(Mone.data[i:i+gap+1])
                print(Mtwo.data[j:j+gap+1])
                print(t_strone)
                print(t_strtwo)
                if(t_strtwo - t_strone == 2):
                    t_condilo.append((i,j))
                j = j + 1
            i = i + 1

        return t_condilo

    def find_seriesid(self,sessions):
        t_total = 0.0
        t_selo = {}
        for session in sessions:
            t_len = len(session)
            if(t_len <= 1):
                continue
            else:
                j = 0
                while(j < t_len -1):
                    pre = session[j][1][-1]
                    last = session[j + 1][1][0]
                    t_total = t_total + 1
                    #los = self.find_senum(pre,last,0,'B','<')
                    los = self.find_senumsub(pre, last, 0, 'B', '>')
                    for lo in los:
                        t_key = str(lo[0]) + ',' + str(lo[1])
                        if lo not in t_selo:
                            t_selo[lo] = 1
                        else:
                            t_selo[lo] = t_selo[lo] + 1
                    j = j + 1
        for key in t_selo:
            if(t_selo[key] / t_total > 0.8):
                print (key)

            def find_seriesid(self, sessions):
                t_total = 0.0
                t_selo = {}
                for session in sessions:
                    t_len = len(session)
                    if (t_len <= 1):
                        continue
                    else:
                        j = 0
                        while (j < t_len - 1):
                            pre = session[j][1][-1]
                            last = session[j + 1][1][0]
                            t_total = t_total + 1
                            los = self.find_senum(pre, last, 0, 'B', '<')
                            for lo in los:
                                t_key = str(lo[0]) + ',' + str(lo[1])
                                if lo not in t_selo:
                                    t_selo[lo] = 1
                                else:
                                    t_selo[lo] = t_selo[lo] + 1
                            j = j + 1
                for key in t_selo:
                    if (t_selo[key] / t_total > 0.8):
                        print(key)



#MessageList = PCAPImporter.readFile('/home/wxw/data/modbus/test_new.pcap').values()
#dealer = message_dealer(MessageList)
#dealer.find_const()
#print (dealer.const)










