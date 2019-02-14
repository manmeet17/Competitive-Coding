from collections import Counter

def odd(d):
    a=[]
    for i in d:
        if d[i]%2!=0:
            a.append((i,d[i]))
    return a

for _ in range(int(input())):
    s=input()
    d=Counter(s)
    arr=odd(d)
    print(d)