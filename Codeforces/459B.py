import math
n=int(input())
l=sorted(list(map(int,input().split())))
if (l[-1]-l[0])==0:
    print (l[-1]-l[0],n*(n-1)//2)
else:
    print (l[-1]-l[0],l.count(l[0])*l.count(l[-1]))
