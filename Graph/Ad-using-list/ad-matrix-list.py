class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={v:[] for v in range(vno)}

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print('Invalid martrix')

    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u]=[(vertex,weight)for vertex,weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v]=[(vertex,weight)for vertex,weight in self.adj_list[v] if vertex!=u]
        else:
            print('Invalid Vertex')
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex,x in self.adj_list[u])
        else:
            print('Invalid martrix')

    def print_adj_list(self):
        for key,value in self.adj_list.items():
            print("V",key,":",value)



if __name__=="__main__":
    G=Graph(5)
    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(2,3)
    G.add_edge(3,4)
    G.add_edge(4,2)
    G.print_adj_list()
    G.remove_edge(1,0)
    G.print_adj_list()
    print(f"Results: {G.has_edge(0,1)}")

