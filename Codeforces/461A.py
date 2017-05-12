import sys
n=int(input())
l=sorted(list(map(int,input().split())))
s=sum(l)
if(len(l)==1):
    print (l[0])
    sys.exit()
while(True):
    s+=l[0]+sum(l[1:])
    del(l[0])
    if(len(l)==1):
        break
print (s)
