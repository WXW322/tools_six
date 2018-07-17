#-*- coding: utf-8 -*-
from netzob.all import *
import sys
sys.path.append("../../")
import t_node
import numpy as np
import random
import math
from matplotlib import pyplot as plt

class words_base:
    def __init__(self):
        print ('xxx')

    def get_loinfo(self,series_list,head_count):
        t_result = {}
        t_length = {}
        i = 0
        while (i < head_count):
            t_result[i] = {}
            t_length[i] = 0
            i = i + 1
        for series in series_list:
            length = len(series)
            i = 0
            while (i < length and i < head_count):
                t_length[i] = t_length[i] + 1
                t_fre = t_result[i]
                t_num = series[i]
                if t_num not in t_fre:
                    t_fre[t_num] = 1
                else:
                    t_fre[t_num] = t_fre[t_num] + 1
                i = i + 1
        i = 0
        while (i < head_count):
            t_pre = t_result[i]
            t_result[i] = sorted(t_pre.items(), key=lambda d: d[1], reverse=True)
            i = i + 1
        return t_result,t_length
