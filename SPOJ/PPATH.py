def seive():
    p=2
    n=10000
    prime=[True for i in range(n)]
    while p*p<=n:
        if prime[p]==True:
            for i in range(p*p,n,p):
                prime[i]=False
        p+=1
    return prime

from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        if u!=v:
            self.graph[u].append(v)

    def bfs(self,s,v):
        if s==v:
            return 0
        vis=[False]*10000
        q=[]
        q.append(s)
        vis[s]=True
        dis=[0]*10000
        while q:
            s=q.pop(0)
            # print("s--->",s)
            for i in self.graph[s]:
                if vis[i]==False:
                    q.append(i)
                    dis[i]=dis[s]+1
                    vis[i]=True
                if i==v:
                    return dis[v]
        return "Impossible"
    
prime=seive()
g=Graph()
for i in range(1000,9999):
    if prime[i]:
        k=list(str(i))
        # print("K--->",k)
        for j in range(4):
            st=0
            if j==0:
                st=1
            for p in range(st,10):
                k[j]=str(p)
                # print(k)
                num=int(''.join(k))
                if prime[num]:
                    g.addEdge(i,num)
            k=list(str(i))


for i in range(int(input())):
    s,d = map(int,input().split())
    print(g.bfs(s,d))
    
