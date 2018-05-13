from netzob.all import *
from treelib import *

def show_tree():
    tt = Tree()
    tt.create_node(tag = '0x11', identifier = '0x11' ,data = 1)
    tt.create_node(tag = '0x12',identifier = '0x12', data = 2, parent = '0x11')
    tt.create_node(tag = '0x13',identifier = '0x13', data = 3, parent = '0x11')
    tt.create_node(tag = '0x14',identifier = '0x14', data = 4, parent = '0x12')
    tt.show()
show_tree()



