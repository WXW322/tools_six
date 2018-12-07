import os
from netzob.all import *


def read_datas(dirs):
    paths = os.listdir(dirs)
    t_datas = []
    t_sedatas = []
    for path in paths:
        t_path = os.path.join(dirs,path)
        t_data = PCAPImporter.readFile(t_path).values()
        t_datas.extend(t_data)
    return t_datas

def get_puredatas(datas):
    t_fdata = []
    for data in datas:
        t_fdata.append(data.data)
    return t_fdata

def get_itoms(string,delimiter):
    return string.split(delimiter)
