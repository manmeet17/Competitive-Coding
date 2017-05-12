import sys
a,b=list(map(int,input().split()))
t=0
if(a==1 and b==1):
    print (0)
    sys.exit(0)
while(a>0 and b>0):
    mi=min(a,b)
    ma=max(a,b)
    a=mi+1
    b=ma-2
    t+=1
print (t)
