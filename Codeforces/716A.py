n,c=map(int,input().split())
l=list(map(int,input().split()))
t=1
for i in range(1,n):
    if(l[i]-l[i-1]<=c):
        t+=1
    else:
        t=1
print (t)
    
