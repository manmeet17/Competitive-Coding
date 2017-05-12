import math
c=list(map(int,input().split()))
m=list(map(int,input().split()))
n=int(input())
t=int(math.ceil(sum(c)/5))
t+=int(math.ceil(sum(m)/10))
if(t<=n):
    print ("YES")
else:
    print ("NO")
