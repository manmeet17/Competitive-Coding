for _ in range(int(input())):
    k=int(input())
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    cm=l[0]+k
    cma=-1
    for i in range(n):
        cm=min(cm,l[i]+k)
        cma=max(cma,l[i]-k)
    print (cma-cm)
