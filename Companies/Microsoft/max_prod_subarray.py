for i in range(int(input())):
    fw=0
    bw=0
    mx=1
    n=int(input())
    l=list(map(int,input().split()))
    for j in range(n):
        mx=mx*l[j]
        if(mx==0):
            mx=1
        fw=max(fw,mx)
    mx=1
    for j in range(n-1,-1,-1):
        mx=mx*l[j]
        if(mx==0):
            mx=1
        bw=max(bw,mx)
    print (max(fw,bw))
