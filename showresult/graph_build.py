from pydotplus import *
from netzob.all import *

class tree_graph:
    def __init__(self,graph_type,datas):
       
        """
        function: init_class
        graph_type: graph_type | tree or graph
        datas: graph datas
        """
        print("aaa")

    def tree2graph(self):
        """
        function: converse tree to graph
        tree: a tree like datas
        graph: a set of nodes and edges
        """
        print("BBB")

    def graph2fig(self,graph_datas,out_dir):
        """
        function: output fig to out_dir
        graph_datas: a set of nodes and edges
        out: a png file
        """
        t_nodes = graph_datas['nodes']
        t_edges = graph_datas['edges']
        t_graph = graphviz.Dot()
        for node in t_nodes:
            t_graph.add_node(node)
        for edge in t_edges:
            t_graph.add_edge(edge)
        #graph = graphviz.graph_from_dot_data(t_graph.getvalue())
        t_graph.write_png("exampleone.png")
    
    def test(self):
        S0 = Node("s0")
        S11 = Node("s11")
        S12 = Node("s12")
        #S13 = Node("s13")
        #S14 = Node("s14")
        S21 = Node("s21")
        S22 = Node("s22")
        S23 = Node("s23")
        S24 = Node("s24")
        Se = Node("se")
        e01 = Edge(S0,S11,label ="Get")
        e02 = Edge(S0,S12,label ="Post")
        #e03 = Edge(S0,S13,label ="Get")
        #e04 = Edge(S0,S14,label ="post")
        e11 = Edge(S11,S21,label ="HTTP 200")
        e21 = Edge(S12,S22,label ="HTTP 200")
        e22 = Edge(S11,S23,label ="HTTP 404")
        e23 = Edge(S12,S24,label ="HTTP 404")
        e31 = Edge(S21,Se,label="")
        e32 = Edge(S22,Se,label="")
        e33 = Edge(S23,Se,label="")
        e34 = Edge(S24,Se,label="")
        t_graph = {}
        t_graph["nodes"] = [S11,S12,S0,S21,S22,S23,S24,Se]
        t_graph["edges"] = [e01,e02,e11,e21,e23,e22,e31,e32,e33,e34]
        self.graph2fig(t_graph,"bbb")

tree = tree_graph("a","B")
tree.test()
