for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    dp=[]
    for j in range(0,n*n,n):
        dp.append(l[j:j+n])
    print(dp)
    for j in range(n-1,-1,-1):
        for k in range(n-1,-1,-1):
            if j==n-1 and k==n-1:
                continue
            print(j,k,dp[j][k])
            if j==0:
                if k==0:
                    dp[j][k]=min(dp[j+1][k], dp[j][k+1])+dp[j][k]
                    continue
                if k==n-1:
                    dp[j][k]=min(dp[j+1][k], dp[j][k-1])+dp[j][k]
                    continue
                else:
                    dp[j][k]=min(dp[j+1][k],dp[j][k-1],dp[j][k+1])+dp[j][k]
                    continue
                
            if j==n-1:
                if k==0:
                    dp[j][k]=min(dp[j-1][k], dp[j][k+1])+dp[j][k]
                    continue
                if k==n-1:
                    dp[j][k]=min(dp[j-1][k], dp[j][k-1])+dp[j][k]
                    continue
                else:
                    dp[j][k]=min(dp[j-1][k] ,dp[j][k-1],dp[j][k+1])+dp[j][k]
                    continue
                    
            if k==0:
                dp[j][k]=min(dp[j-1][k],dp[j+1][k] ,dp[j][k+1])+dp[j][k]
                continue
            
            if k==n-1:
                dp[j][k]=min(dp[j-1][k],dp[j+1][k], dp[j][k-1])+dp[j][k]
                continue
            
            else:
                dp[j][k]=min(dp[j-1][k],dp[j+1][k],dp[j][k-1],dp[j][k+1])+dp[j][k]
    print(dp)
                
            