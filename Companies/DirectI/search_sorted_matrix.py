for _ in range(int(input())):
    n,m=map(int,input().split())
    mat=[[0 for i in range(m)] for j in range(n)]
    l=list(map(int,input().split()))
    x=int(input())
    k=0
    for i in range(n):
        for j in range(m):
            mat[i][j]=l[k]
            k+=1
    f=0
    i=0
    j=m-1
    # print(mat)
    # print("X---->",x)
    while(f!=1):
        if i>n-1 or j<0:
            break
        curr=mat[i][j]
        # print("Curr--->",curr)
        if curr>x:
            j-=1
        if curr<x:
            i+=1
        if curr==x:
            f=1
            print(1)
    if f==0:
        print (0)
