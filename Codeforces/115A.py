from collections import defaultdict as dd
class Graph:
    def __init__(self,n):
        self.graph=dd(list)
        self.n=n
        self.vis=[False]*(n+1)
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def bfs(self,u):
        q=[u]
        lvl=[0]*(self.n+1)
        lvl[u]=1
        while len(q)>0:
            f=q.pop()
            # print("I--->",f)
            for i in self.graph[f]:
                if self.vis[i]==False:
                    self.vis[i]=True
                    q.append(i)
                    lvl[i]=lvl[f]+1
        # print(lvl)
        return max(lvl)


n=int(input())
g=Graph(n)
l=[]
for i in range(n):
    x=int(input())
    if x==-1:
        l.append(i+1)
        continue
    g.add_edge(x,i+1)
# print(g.graph)
ans=-float("inf")
for i in l:
    k=g.bfs(i)
    # print(i,k)
    if k!=1:
        ans=max(ans,k)
if ans==-float("inf"):
    ans=1
print(ans)