for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=""
    for i in range(n):
        if l[i]<=k:
            s+="1"
            k-=l[i]
        else:
            s+="0"
    print(s)