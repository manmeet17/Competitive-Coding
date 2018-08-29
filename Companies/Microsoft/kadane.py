for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=-100000007
    cm=0
    s=0
    for j in range(n):
        cm=max(l[j],l[j]+cm)
        m=max(cm,m)
    print (m)
