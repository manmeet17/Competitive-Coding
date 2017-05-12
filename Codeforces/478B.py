n,m=map(int,input().split())

mx=((n-m+1)*(n-m))//2

x=n//m
mn=(x*(x-1))//2
mn*=m
mn+=x*(n%m)

print(mn,mx)
