def block(a,k):
    b=[a[0]]
    if len(a)==1:
        if k<=1:
            return 1
        else:
            return 0
    r=1
    t=0
    f=False
    for i in range(1,len(a)):
        if a[i]==b[-1]:
            f=True
            r+=1
        else:
            if r>=k:
                t+=1
            b.append(a[i])
            f=False
            r=1
            if(i==len(a)-1):
                if r>=k:
                    t+=1
    if f==True:
        if r>=k:
            t+=1
    return t
for i in range(int(input())):
    n,q=map(int,input().split())
    s=list(map(int,input().split()))
    for j in range(q):
        l,r,k=map(int,input().split())
        p=s[l-1:r]
        print (block(p,k))
        
