def ans(a,b):
    ans=0
    for i in range(1,10):
        if( i in a and i in b):
            ans=ans*10+i
    return ans
for i in range(int(input())):
    n1,n2=list(map(int,input().split()))
    l=list()
    p=0
    for j in range(n1+n2):
        l.append(input())
    for j in range(n1):
        for k in range(n1,n1+n2):
            if(ans(l[j],l[k])%2==0):
                p+=1
    print (p/(n1*n2))
