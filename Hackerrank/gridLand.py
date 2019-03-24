from collections import defaultdict
n,m,k=map(int,input().split())
d=defaultdict(list)
for i in range(k):
    r,c1,c2=map(int,input().split())
    d[r-1].append((c1-1,c2-1))
ans=0
for i in d:
    p=d[i]
    lp=len(p)
    p=sorted(p, key=lambda x: x[0])
    mi=p[0][0]
    ma=p[0][1]
    get=0
    for j in range(1,lp):
        if p[j][0]<=ma:
            ma=max(p[j][1],ma)
        else:
            get+=ma-mi+1
            mi=p[j][0]
            ma=p[j][1]
        # print(mi,ma,get,p[j])
    get+=ma-mi+1
    ans+=get
print(m*n-ans)