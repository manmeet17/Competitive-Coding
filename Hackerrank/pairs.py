from collections import Counter
n,k=map(int,input().split())
l=list(map(int,input().split()))
d=Counter(l)
ans=sum([d[i-k] for i in d if i-k in d])
print(ans)