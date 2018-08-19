for i in range(int(input())):
    n=int(input())
    W=int(input())
    wt=list(map(int,input().split()))
    val=list(map(int,input().split()))
    K=[[0 for j in range(W+1)] for k in range(n+1)]
    for j in range(n+1):
        for w in range(W+1):
            if j==0 or w==0:
                K[j][w]=0
            elif wt[j-1]<=w:
                K[j][w]=max(val[j-1]+K[j-1][w-wt[j-1]], K[j-1][w])
            else:
                K[j][w]=K[j-1][w]
    print (K[-1][-1])
