import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import sys


class train_data:
    def __init__(self,data_num,file_name):
        self.data_num = data_num
        self.models = []
        self.filename = file_name
        self.data_right = None
        self.data_wrong = None
        self.data_valid = None
        self.datas = None
        self.outdata = None

    def get_dataset(self):
        data = pd.read_csv(self.filename)
        data = data.sample(frac = 1).reset_index(drop = True)
        self.data_right = data[data['lable'] == 1]
        self.data_wrong = data[data['lable'] == 0]
        length_r = self.data_right.shape[0]
        length_w = self.data_wrong.shape[0]
        self.data_valid = self.data_right[0:int(length_r/10)]
        self.data_right = self.data_right[int(length_r/10):]
        self.data_valid = pd.concat([self.data_valid,self.data_wrong[0:int(length_r/10)]])
        self.data_wrong = self.data_wrong[int(length_r/10):]
        i = 0
        self.datas = []
        while(i < self.data_num):
            data_temp = self.data_wrong.sample(frac = 0.1)
            self.datas.append(data_temp)
            i = i + 1
        return self.data_right,self.datas

    def get_transdata(self,filename):
        self.outdata = pd.read_csv(filename)

    def crossvalidate(self,features,lable):
        i = 0
        while(i < self.data_num):
            model_temp = self.models[i]
            print (model_temp.score(self.data_valid[features],self.data_valid[lable]))
            i = i + 1


    def transvalidate(self,features,lable):
        i = 0
        while(i < self.data_num):
            model_temp = self.models[i]
            print (model_temp.score(self.outdata[features],self.outdata[lable]))
            i = i + 1





    def get_tempdata(self):
        data = pd.read_csv(self.filename)
        self.data_right = data[data['lable'] == 1]
        self.data_wrong = data[data['lable'] == 0]
        length_r = self.data_right.shape[0]
        length_w = self.data_wrong.shape[0]
        self.data_valid = self.data_right[0:length_r/10]
        self.data_right = self.data_right[length_r/10:]
        self.data_valid = pd.concat([self.data_valid,self.data_wrong[0:length_r/10]])
        self.data_wrong = self.data_wrong[length_r/10:]
        i = 0
        self.datas = []
        length_one = self.data_right.shape[0]
        length_two = self.data_wrong.shape[0]
        t_num = length_two/length_one
        pre = 0
        while(i < t_num):
            data_temp = self.data_wrong[pre:pre+length_one]
            self.datas.append(data_temp)
            pre = pre + length_one
            i = i + 1
        self.datas.append(self.data_wrong[pre:])
        return self.data_right,self.datas

    def get_models(self,features,lable):
        i = 0
        #data_right,data_wrong = self.get_dataset()
        #while(i < self.data_num):
        while (i < len(self.datas)):
            models_temp = MLPClassifier(hidden_layer_sizes=(40,40),activation='relu',solver='adam')
            data_new = pd.concat([self.data_right,self.datas[i]])
            i = i + 1
            models_temp.fit(data_new[features],data_new[lable])
            self.models.append(models_temp)

    def validate(self,features,lable):
        i = 0
        while(i < self.data_num):
            model_temp = self.models[i]
            print (model_temp.score(self.data_valid[features],self.data_valid[lable]))
            i = i + 1

    def tran_learning(self,features,lable,out_data):
        i = 0
        while(i < self.data_num):
            model_temp = self.models[i]
            print (model_temp.score(out_data[features],out_data[lable]))
            i = i + 1











data = pd.read_csv('/home/wxw/data/modbus_train/lable_finalone.csv')
feature = data.columns.values.tolist()
feature.remove('value')
feature.remove('lable')
tt = train_data(5,'/home/wxw/data/modbus_train/lable_finalone.csv')
tt.get_dataset()
tt.get_models(feature,'lable')
#tt.validate(feature,'lable')
tt.get_transdata('/home/wxw/data/iec104_train/lable_finalone.csv')
tt.transvalidate(feature,'lable')
