for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    s=int(input())
    dp=[[0 for j in range(s+1)] for k in range(n+1)]
    for j in range(n+1):
        for k in range(s+1):
            if(j==0):
                dp[j][k]=0
            else:
                if(k<l[j-1]):
                    dp[j][k]=dp[j-1][k]
                elif(k==l[j-1]):
                    dp[j][k]=dp[j-1][k]+1
                else:
                    dp[j][k]=dp[j-1][k]+dp[j][k-l[j-1]]
    print (dp[-1][-1])
