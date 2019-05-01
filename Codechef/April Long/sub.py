from collections import defaultdict as dd
for _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    d=dd(set)
    # vals={i+1:l[i] for i in range(n)}
    # print(vals)
    for i in range(n-1):
        x,y=map(int,input().split())
        d[x].add(y)
    print(d)
    for i,j in d.items():
        l[i-1]+=sum([l[k-1] for k in j])
        # for k in j:
        #     l[i-1]+=l[k-1]
        # vals[i]=sum([l[x-1] for x in d[i]])
    print(l)
    # print(vals)
    