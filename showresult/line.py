import matplotlib.pyplot as plt
import os
import sys

def plot_linefigure(file_to,x_lable,y_lable,datas_X,datas_Y,colors,labels,makers):
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    t_len = len(datas_X)
    i = 0
    while(i < t_len):
        show_variable('y'+str(i),datas_Y[i],'w+')
        plt.plot(datas_X[i],datas_Y[i],colors[i],label = labels[i],marker = makers[i])
        i = i + 1

    plt.legend()
    path = os.path.join(file_to,'line.jpg')
    plt.savefig(path)



def process_data(file_from,file_to,x_lable,y_lable):
    t_correct = {}
    t_preci = {}
    t_coms = {}
    for filename in os.listdir(file_from):
        t_file = os.path.join(file_from,filename)
        #print(t_file)
        t_filein = open(t_file,'r')
        t_line = t_filein.readline()
        #print(t_line)
        t_line = t_line[0:-1]
        t_temp = t_line.split(' ')
        t_id = int(t_temp[-4])
        t_cor = float(t_temp[-3])
        t_pre = float(t_temp[-2])
        t_com  = float(t_temp[-1])
        t_cor = round(t_cor,4)
        t_pre = round(t_pre,4)
        t_com  = round(t_com,4)
        t_correct[t_id] = t_cor
        t_preci[t_id] = t_pre
        t_coms[t_id] = t_com
    #show_variable('yy',t_correct,'a+')
    #show_variable('yy',t_preci,'a+')
    #show_variable('yy',t_coms,'w+')
    t_correct = sorted(t_correct.items(),key = lambda x:x[0])
    datas_X = []
    datas_Y = []
    x_temp = []
    y_temp = []
    colors = []
    labels = []
    makers = []
    for key in t_correct:
        x_temp.append(key[0])
        y_temp.append(key[1])
    datas_X.append(x_temp)
    datas_Y.append(y_temp)
    colors.append('r')
    labels.append('correct')
    makers.append('o')
    x_temp = []
    y_temp = []
    t_preci = sorted(t_preci.items(),key = lambda x:x[0])
    for key in t_preci:
        x_temp.append(key[0])
        y_temp.append(key[1])
    datas_X.append(x_temp)
    datas_Y.append(y_temp)
    colors.append('b')
    labels.append('precision')
    #show_variable('Y',datas_Y,'w+')
    t_coms = sorted(t_coms.items(),key = lambda x:x[0])
    x_temp = []
    y_temp = []
    for key in t_coms:
        x_temp.append(key[0])
        y_temp.append(key[1])
    datas_X.append(x_temp)
    datas_Y.append(y_temp)
    makers.append('+')
    #show_variable('X',datas_X,'w+')
    #show_variable('Y',datas_Y,'w+')
    colors.append('g')
    labels.append('combine')
    makers.append('s')
    plot_linefigure(file_to,x_lable,y_lable,datas_X,datas_Y,colors,labels,makers)    

def show_variable(file_to,val,type):
    tempout = sys.stdout
    file = open(file_to,type)
    sys.stdout = file
    print(val)
    sys.stdout = tempout


file_from = sys.argv[1]
file_to = sys.argv[2]
process_data(file_from,file_to,'threshold T',"rate")


        

        





