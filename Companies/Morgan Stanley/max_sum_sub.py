for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=l[:]
    for j in range(1,n):
        for k in range(0,j+1):
            if(l[k]<l[j]):
                s[j]=max(s[j],l[j]+s[k])
    print (max(s))
