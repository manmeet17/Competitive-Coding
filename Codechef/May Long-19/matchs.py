from math import gcd

def solve(n,m):
    if n%m==0 or m%n==0:
        return 1
    a=max(n,m)
    b=min(n,m)
    while a%b!=0 or b%a!=0:
        x=gcd(a,b)
        a/=x
        b/=x


for _ in range(int(input())):
    n,m=map(int,input().split())
    ans=solve(n,m)