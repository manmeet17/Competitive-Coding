n,k=list(map(int,input().split()))
k=240-k
c=0
i=0
while(k>=5*(i+1) and i<=n):
    k-=5*(i+1)
    i+=1
if(i>n):
    print (n)
else:
    print (i)
