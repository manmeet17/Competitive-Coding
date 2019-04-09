import functools
import operator
n,q=map(int,input().split())
l=list(map(int,input().split()))
xor=functools.reduce(operator.xor, l)
print(xor)
for i in range(n,1000):
    xor^=l[-1]
    l.append(xor)
print(l)