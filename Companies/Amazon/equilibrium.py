for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(n==1):
        print (n)
        continue
    ls=0
    rs=sum(l[1:])
    if(ls==rs):
        print (0)
        continue
    f=0
    for j in range(1,n):
        ls+=l[j-1]
        rs-=l[j]
        if(ls==rs):
            f=1
            print (j+1)
            break
    if(f==0):
        print (-1)
    
