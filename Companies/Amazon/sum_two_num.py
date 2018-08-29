def add(n,m,a,b):
    carry=0
    sums=""
    while(m>=0):
        s=a[n]+b[m]+carry
        # print (s,m)
        if(s>9):
            s=str(s)
            carry=int(s[0])
            sums+=s[1]
                
        else:
            sums+=str(s)
            carry=0
        m-=1
        n-=1
    return (sums,carry)

for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if(n>=m):
        s=add(n-1,m-1,a,b)
        print ("S---->",s)
        if n==m:
            s=list(str(int(str(s[1])+s[0][::-1])))
        else:
            a[n-m-1]+=s[1]
            s=a[:n-m]+list(s[0][::-1])
    else:
        s=add(m-1,n-1,b,a)
        b[m-n-1]+=s[1]
        s=b[:m-n]+list(s[0][::-1])
    # print (int(s[::-1]))
    print (s)
