for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    d={}
    f=0
    for i in range(n):
        d[l[i]]=1
        if(k-l[i] in d):
            print ("Yes")
            f=1
            break
    if(f==0):
        print ("No")
