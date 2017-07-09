def solve(dp,a,n):
    for i in range(2,n):
        dp[i]=max(dp[i-2]+a[i],dp[i-1])
    return dp
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(len(l)<=2):
        if(len(l)==1):
            print ("Case "+str(i+1)+": "+str(l[0]))
        elif (len(l)==2):
            print ("Case "+str(i+1)+": "+str(max(l[0],l[1])))
        continue
    dp=[0]*n
    dp[0]=l[0]
    dp[1]=max(l[0],l[1])
    dp=solve(dp,l,n)
    print ("Case "+str(i+1)+": "+str(dp[n-1]))
