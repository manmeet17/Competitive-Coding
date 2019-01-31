from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,u):
        q=[]
        vis=[False]*len(self.graph)
        q.append(u)
        vis[u]=True
        while q:
            s=q.pop(0)
            print (s,end=' ')
            for i in self.graph[s]:
                if vis[i]==False:
                    q.append(i)
                    vis[i]=True

g=Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 0)") 
g.bfs(0)
print()
