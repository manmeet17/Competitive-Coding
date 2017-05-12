n=int(input())
m=0
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
for i in range(n):
    k=l[i]*(n-i)
    if k>m:
        m=k
print (m)
