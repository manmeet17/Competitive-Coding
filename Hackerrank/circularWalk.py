#!/bin/python3

import sys
from collections import defaultdict

def make_graph(arr,n):
    graph=defaultdict(set)
    for i in range(n):
        for j in range(1,arr[i]+1):
            graph[i].add((i+j)%(n))
            if i-j<0:
                graph[i].add(n-1+(i-j)+1)
            else:
                graph[i].add(i-j)
    return graph

def bfs(graph,s,t,n):
    vis=[False]*n
    lvl=[0]*n
    q=[s]
    vis[s]=True
    while len(q)>0:
        f=q.pop(0)
        for i in graph[f]:
            if vis[i]==False:
                vis[i]=True
                lvl[i]=lvl[f]+1
                q.append(i)
                # print(lvl)
                if i==t:
                    return lvl[i]
    return -1                
                
def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    arr=[0]*n
    arr[0]=r_0
    for i in range(1,n):
        arr[i]=(arr[i-1]*g+seed)%p
    # print(arr)
    if s==t:
        return 0
    graph = make_graph(arr,n)
    # print(graph)
    return bfs(graph,s,t,n)

n, s, t = input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)