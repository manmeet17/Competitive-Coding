for i in range(int(input())):
    n,k=map(int,input().split())
    dp=[[0 for p in range(n)] for j in range(k)]
    for p in range(k):
        dp[p][0]=p+1
    for j in range(1,n):
        for p in range(k):
            l=[]
            if(p<j):
                dp[p][j]=dp[p][j-1]
                continue
            for q in range(p+1):
                if q==0:
                    l.append(1+max(0,dp[p-q-1][j]))
                elif q==p:
                    l.append(1+max(dp[q-1][j-1],0))
                else:
                    l.append(1+max(dp[q-1][j-1],dp[p-q-1][j]))
            dp[p][j]=min(l)
    print (dp[-1][-1])