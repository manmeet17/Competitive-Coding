import random
from collections import defaultdict
d={}
for _ in range(1000000):
    a=[1,2,3,4,5,6,7,8]
    for i in range(len(a)):
        r=random.randint(0,len(a)-1)
        a[i],a[r]=a[r],a[i]
    s="".join([str(k) for k in a])
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
print (list(sorted(d.items(),key=lambda x:x[1]))[-1])