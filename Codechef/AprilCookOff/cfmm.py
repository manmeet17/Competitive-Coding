from collections import defaultdict as dd
for k in range(int(input())):
    d=dd(int)
    n=int(input())
    for i in range(n):
        s=input()
        for j in s:
            if j in 'codechef':
                d[j]+=1
    # d=sorted(d.items(), key=lambda x: x[1])
    d['c']=d['c']//2
    d['e']=d['e']//2
    # print(d)
    m=10**7
    for i in 'codechef':
        m=min(m,d[i])
        # d[i]-=1
    print(m)