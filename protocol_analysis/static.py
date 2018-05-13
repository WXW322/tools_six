import matplotlib.pyplot as plt
import numpy as np
from netzob.all import *
import struct

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')


class protocol_dis:
    def __init__(self,filename):
        self.datas = PCAPImporter.readFile(filename).values()

    def get_lodata(self,t_lo):
        details = {}
        for i in range(0,256):
            details[i] = 0
        for data in self.datas:
            num = struct.unpack('>h',self.datas[t_lo])
            details[num] = details[num] + 1
        temp_x = []
        temp_y = []
        for key in details:
            temp_x.append(key)
            temp_y.append(details[key])
        result = {}
        result['x'] = temp_x
        result['y'] = temp_y
        return result

    def get_singlepic(self,datas):
        plt.plot(datas['x'],datas['y'])
        plt.show()




