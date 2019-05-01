# def solve(n):
#     for i in range(n):
#         k=list(map(int,input().split()))
#         if 0 not in k:
#             return 0
#     return 1
import numpy as np

for _ in range(int(input())):
    n=int(input())
    mat=[]
    for i in range(n):
        mat.append(list(map(int,input().split())))
    mat=np.matrix(mat)
    cols=np.all(mat,axis=0)
    rows=np.all(mat,axis=1)
    if ~np.any(rows) and ~np.any(cols):
        print("YES")
    else:
        print("NO")
