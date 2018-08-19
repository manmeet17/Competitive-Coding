for i in range(int(input())):
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    tot=0
    p=0
    f=0
    for j in range(n):
        tot+=l[j]
        while(tot>s):
            tot-=l[p]
            p+=1
        if(tot==s):
            print (p+1,j+1)
            f=1
            break
    if f==0:
        print (-1)s
