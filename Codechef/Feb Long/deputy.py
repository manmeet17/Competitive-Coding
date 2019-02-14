for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=list(map(int,input().split()))
    ans=-1
    for i in range(n):
        if i==0:
            if a[n-1]+a[i+1]<d[i]:
                ans=max(ans,d[i])
        if i==n-1:
            if a[0]+a[i-1]<d[i]:
                ans=max(ans,d[i])
        else:
            if a[i-1]+a[i+1]<d[i]:
                ans=max(ans,d[i])
    print(ans)