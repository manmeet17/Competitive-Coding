from math import gcd
def lcm(a,b):
    return (a*b)//gcd(a,b)

for _ in range(int(input())):
    n,a,b,k=map(int,input().split())

    if (n//a) + (n//b) - 2*(n//lcm(a,b)) >= k:
        print("Win")
    else:
        print("Lose")