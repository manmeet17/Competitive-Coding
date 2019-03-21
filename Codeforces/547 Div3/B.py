n=int(input())
l=list(map(int,input().split()))
m=-1
c=0
last=0
first=0
f=0
for i in range(n):
    if l[i]==0:
        c=0
        if f==0:
            first=i
            f=1    
    else:
        c+=1
        if i==n-1:
            last=c
    m=max(m,c)
print(max(m,first+last))