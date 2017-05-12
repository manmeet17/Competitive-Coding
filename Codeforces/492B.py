import sys
n,l=map(int,input().split())
k=[]
s=sorted(list(map(int,input().split())))
if(n==1):
    p=max(s[0]-0,l-s[-1])
    print ("%.10f"%p)
    sys.exit(0)
for i in range(n-1):
    k.append((s[i+1]-s[i])/2)
p=max(max(k),max(s[0]-0,l-s[-1]))
print ("%.10f"%p)
