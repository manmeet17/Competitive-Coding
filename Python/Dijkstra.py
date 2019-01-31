from collections import defaultdict
import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]

    def printSol(self, dist):
        for i in range(self.V):
            print (i,"\t",dist[i])

    def minDist(self,dist,spSet):
        min=sys.maxsize
        for i in range(self.V):
            if dist[i]<min and spSet[i]==False:
                min=dist[i]
                min_index=i
        return min_index

    def dijkstra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        spSet = [False]*self.V

        for i in range(self.V):
            u=self.minDist(dist,spSet)
            spSet[u]=True
            for v in range(self.V):
                if self.graph[u][v]>0 and spSet[v]==False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]

        self.printSol(dist)

g=Graph(4)
g.graph=[[0,4,3,0],
         [4,0,0,2],
         [3,0,0,0],
         [0,2,0,0]]
g.dijkstra(0)