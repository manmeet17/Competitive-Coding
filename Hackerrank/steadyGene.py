from collections import Counter, defaultdict
n=int(input())
s=input()
k=n//4
d=Counter(s)

def check(d,k):
    return all(map(lambda x: x[1]==k, d.items()))

def solve(d,k):
    if check(d,k):
        return 0
    for i in s:
        