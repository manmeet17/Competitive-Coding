import math
def solve(n,k,l):
    c=0
    for i in range(n):
        for j in range(i,n):
            p=l[i:j+1]
            if j-i+1<1:
                continue
            m=math.ceil(k/(j-i+1))
            # print(p,j-i+1,m)
            s=list(sorted(p*m))
            # print("S---->",s, len(s))
            if k-1<0 or k-1>=m*(j-i+1):
                continue
            x=s[k-1]
            f=p.count(x)
            # print("X--->",x,f)
            if f in p:
                c+=1
            #     print("C--->",c)
            # print("\n")
    return c

for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    print(solve(n,k,l))