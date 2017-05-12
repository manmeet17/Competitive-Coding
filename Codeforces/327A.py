def flip(a,i,j):
    for i in range(i,j):
        a[i]=1-a[i]
    print (a)
    return a.count(1)
n=int(input())
s=list(map(int,input().split()))
l=list()
for i in range(n):
    for j in range(i+1,n):
        l.append(flip(s,i,j))
        print (i,j,l[-1])
print (max(l))
print (l)
