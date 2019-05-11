from math import gcd
from collections import defaultdict as dd

class Graph:
    def __init__(self):
        self.graph=dd(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)

def solve(n,m):
    if n%m==0 or m%n==0:
        return 1
    a=max(n,m)
    b=min(n,m)
    g=Graph()
    def build(g,n,m):
        if n%m==0 or m%n==0:
            return 1
        while n!=0 or m!=0:
            
        
    

    while a%b!=0 or b%a!=0:
        x=gcd(a,b)
        a/=x
        b/=x


for _ in range(int(input())):
    n,m=map(int,input().split())
    ans=solve(n,m)