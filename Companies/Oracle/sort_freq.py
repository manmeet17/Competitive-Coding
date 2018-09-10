from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    d=defaultdict(int)
    l=list(map(int,input().split()))
    for i in l:
        d[i]+=1
    k=sorted(d, key=lambda k: (d[k], -k), reverse=True)
    # print (k)
    for i in k:
        s=(str(i)+' ')*d[i]
        print (s,end='')
    print()
