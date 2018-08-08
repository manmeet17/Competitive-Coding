for i in range(int(input())):
    n=int(input())
    f=0
    l=list(map(int,input().split()))
    lmax=[l[0]]+[0]*(n-1)
    rmin=[0]*(n-1)+[l[-1]]
    for j in range(1,n):
        lmax[j]=max(lmax[j-1],l[j])
    for j in range(n-2,-1,-1):
        rmin[j]=min(rmin[j+1],l[j])
    for j in range(1,n-1):
        if lmax[j]<=l[j]<=rmin[j]:
            print (l[j])
            f=1
            break
    if(f==0):
        print (-1)
