for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    p=list(map(int,input().split()))
    l.sort()
    p.sort()
    t=1
    for j in range(n):
        if l[j]!=p[j]:
            t=0
            break
    print (int(t==1))
