from collections import Counter
n,m=map(int,input().split())
l=[]
for i in range(m):
    s=list(map(int,input().split()))
    l.append(s.index(max(s))+1)
d=Counter(l)
print (d.most_common(1)[0][0])
