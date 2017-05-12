n,d=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
i=c=0
while(i<n-1):
    if (l[i+1]-l[i])<=d:
        c+=1
        i+=2
    else:
        i+=1
print (c)
