import networkx as nx
import matplotlib.pyplot as plt
class Node:
    def __init__(self,nodeName,nodeData=None):
        self.nodeName=nodeName
        self.nodeData=nodeData
        pass

class Edge:
    def __init__(self,edgeName,nodeStart,nodeEnd):
        self.edgeName=edgeName
        self.nodeStartName=nodeStart.nodeName
        self.nodeEndName=nodeEnd.nodeName
        pass

class MyGraph:
    def __init__(self):
        self.nodeList=[]
        self.edgeList=[]
        self.nodeNameList=[]
        self.edgeNameList=[]


    def create_graph(self,nlist,elist):
        for node in nlist:
            self.nodeList.append(node)
            self.nodeNameList.append(node.nodeName)

        for edge in elist:
            self.edgeList.append(edge)
            self.edgeNameList.append(edge.edgeName)

        # print(self.nodeNameList,self.edgeNameList)

    def add_node(self,node,edge):
        if  node.nodeName in self.nodeNameList:
            print('node %s already exist' % node.nodeName)
            return

        self.nodeList.append(node)
        self.edgeList.append(edge)
        self.nodeNameList.append(node.nodeName)
        self.edgeNameList.append(edge.edgeName)
        # print(self.nodeNameList, self.edgeNameList)

    def del_node(self,node_name):
        for node1 in self.nodeList:
            if node_name==node1.nodeName:
                self.nodeList.remove(node1)
                self.nodeNameList.remove(node1.nodeName)
        # print(len(self.edgeList))
        # print(self.nodeNameList, self.edgeNameList)
        for ed in self.edgeList:
            # print(ed.edgeName)
            if ed.nodeStartName==node_name:

                self.edgeList.remove(ed)
                self.edgeNameList.remove(ed.edgeName)
            if ed.nodeEndName==node_name:
                self.edgeList.remove(ed)
                self.edgeNameList.remove(ed.edgeName)

        # print(self.nodeNameList, self.edgeNameList)

    def change_egde(self,edge_name,new_start,new_end): #改变一条边的起点或终点
        for ed in self.edgeList:
            if ed.edgeName==edge_name:
                ed.nodeStartName=new_start
                ed.nodeEndName = new_end


    def check_node(self,node_name): #查询某个节点是否存在,存在则返回该节点所有的父节点和子节点名称
        if not node_name in self.nodeNameList:
            print('node %s is not exist' % node_name)
            return

        parent_node_name=[]
        children_node_name=[]

        for ed in self.edgeList:
            if ed.nodeStartName==node_name:
                children_node_name.append(ed.nodeEndName)

            if ed.nodeEndName==node_name:
                parent_node_name.append(ed.nodeStartName)

        return parent_node_name,children_node_name

    def get_node(self,node_name):
        for no in self.nodeList:
            if no.nodeName==node_name:
                return no
    def get_neighbor_node(self,node_name):

        parent_node_name, children_node_name=self.check_node(node_name)

        return  list(set(parent_node_name+children_node_name))


    def dfs(self,start_node_name,end_node_name):
        nodeSetName=set()
        stack=[]
        path=[]
        path.append(start_node_name)
        node_start=self.get_node(start_node_name)
        nodeSetName.add(start_node_name)
        stack.append(node_start)
        while len(stack)>0:
            current_node=stack.pop()

            _,currentNodeName=self.check_node(current_node.nodeName)
            for child in currentNodeName:
                if child not in nodeSetName:
                    if child==end_node_name:
                        path.append(end_node_name)
                        # print("founded")
                        # print(path)
                        return path
                    stack.append(current_node)
                    stack.append(self.get_node(child))
                    nodeSetName.add(child)
                    path.append(child)
                    break
    def bfs(self,start_node_name,end_node_name):
        queue=[]
        path=[]
        queue.insert(0,self.get_node(start_node_name))
        while queue:
            currentNode=queue.pop()
            path.append(currentNode.nodeName)
            _, currentNodeNamelist = self.check_node(currentNode.nodeName)
            if currentNode.nodeName==end_node_name:
                return path
            for child_name in currentNodeNamelist:
                queue.insert(0,self.get_node(child_name))

        return path


    def show_graph(self,path=None):
        self.showgraph = nx.DiGraph()
        edge_list = []
        for each_edge in self.edgeList:
            # print(tuple([each_edge.nodeStartName,each_edge.nodeEndName]))
            edge_list.append(tuple([each_edge.nodeStartName, each_edge.nodeEndName]))
        self.showgraph.add_edges_from(edge_list)
        # self.showgraph.add_edge('E','C',{'color':'red'})
        # print(edge_list)
        if path==None:


            nx.draw(self.showgraph, pos=nx.circular_layout(self.showgraph),with_labels=True)
            plt.show()
        else:
            # print(path)
            edge_color=['b']*len(self.edgeNameList)
            i=0
            for edge_couple in edge_list:
                # print(edge_couple)
                if len(path) >1:
                    if edge_couple[0]==path[0] and edge_couple[1]==path[1]:
                        edge_color[i]='r'
                        path.pop(0)
                i += 1
            # print(edge_color)
            nx.draw(self.showgraph, pos=nx.circular_layout(self.showgraph),with_labels=True,edge_color=tuple(edge_color))
            plt.show()

        # for each_node_name in self.nodeNameList:
        #     self.showgraph.add_node(each_node_name)
        # for each_edge in self.edgeList:
        #     self.showgraph.add_edge(each_edge.nodeStartName,each_edge.nodeEndName)
        # nx.draw(self.showgraph,with_labels=True,pos=nx.circular_layout(self.showgraph))
        # plt.show()


nodea = Node('A', 45)
nodeb = Node('B', 26)
nodec = Node('C', 16)
noded = Node('D', 84)
nodee = Node('E', 90)
nodef = Node('F', 23)

nodeg = Node('G', 96)

edge1 = Edge('1', nodea, nodeb)
edge2 = Edge('2', nodeb, nodef)
edge3 = Edge('3', nodec, nodeb)
edge4 = Edge('4', nodef, noded)
edge5 = Edge('5', noded, nodef)
edge6 = Edge('6', nodec, noded)
edge7 = Edge('7', noded, nodec)
edge8 = Edge('8', nodec, nodea)
edge9 = Edge('9', nodea, nodee)

edge10 = Edge('10', nodeg, nodee)


class Tester:
    def __init__(self):
        self.graph=MyGraph()
        self.graph.create_graph([nodea,nodeb,nodec,noded,nodee,nodef],[edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9])
        self.graph.show_graph()
        # print(self.graph.nodeNameList, self.graph.edgeNameList)

    def testGraphAddNode(self):
        self.graph.add_node(nodeg,edge10)
        self.graph.show_graph()
        # print(self.graph.nodeNameList, self.graph.edgeNameList)

    def testGraphdDelNode(self):

        self.graph.del_node('E')
        self.graph.show_graph()
        # print(self.graph.nodeNameList,self.graph.edgeNameList)

    def testGrapgChange_edge(self):
        # print(self.graph.check_node('E'))
        # print(self.graph.check_node('C'))
        self.graph.change_egde('1','E','C')
        self.graph.show_graph()
        # print(self.graph.check_node('E'))
        # print(self.graph.check_node('C'))

    def testGraphCheckNode(self):
        print(self.graph.check_node('A'))

    def testDfs(self):
        path=self.graph.dfs('A', 'D')
        print('A 到 D 的路径（dfs）是 %s'%path)
        # self.graph.show_graph(path)

    def testBfs(self):
        path=self.graph.bfs('A','D')
        print('A 到 D 的路径（bfs）是 %s'%path)
        # self.graph.show_graph(path)

    def testGetNeighborNodes(self):
        print(self.graph.get_neighbor_node('A'))
if __name__ == '__main__':
    test=Tester() #生成一个图
    # test.testDfs() #返回路径
    # test.testBfs() #返回路径
    # test.testGraphAddNode() #添加节点G,画图
    test.testGraphdDelNode() #删除节点G,画图
    # test.testGrapgChange_edge() #改变边‘1’的起、始节点，画图
    # test.testGraphCheckNode() #查询节点A的所有父节点和子节点
    # test.testGetNeighborNodes() #查询A附近节点




