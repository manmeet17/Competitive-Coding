def readInps():
    return map(int,input().split())

class Node:
    def __init__(self, val):
        self.val=val
        self.tot=0
        self.children=[]
    
    def add_child(self, obj):
        self.children.append(obj)

def solve(d, ans):
    root=d[1]
    
    return


for _ in range(int(input())):
    n,x=readInps()
    l=list(readInps())
    ans=sum(l)
    d={}
    for i in range(n):
        d[i+1]=Node(l[i])
    for i in range(n-1):
        a,b=readInps()
        d[a].add_child(d[b])
    solve(d,ans)