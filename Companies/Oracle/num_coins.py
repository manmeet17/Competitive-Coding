for i in range(int(input())):
    v,n=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    dp=[[0 for j in range(v+1)] for k in range(n)]
    for j in range(n):
        for k in range(v+1):
            # print (j,k)
            if k<l[j]:
                if k==0:
                    dp[j][k]=0
                    continue
                if j==0:
                    dp[j][k]=100007
                else:
                    dp[j][k]=dp[j-1][k]
            else:
                if j==0:
                    if k%l[j]!=0:
                        dp[j][k]=100007
                    else:
                        dp[j][k]=k/l[j]
                else:
                    dp[j][k]=min(dp[j-1][k],dp[j][k-l[j]]+1)
    print (int(dp[-1][-1]))
