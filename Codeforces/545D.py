n=int(input())
d=0
l=sorted(list(map(int,input().split())))
s=l[0]
for i in range(1,n):
    if(l[i]<s):
        d+=1
    s+=l[i]
print (n-d)
