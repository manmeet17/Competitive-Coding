n,k=map(int,input().split())
l=[]
for i in range(n):
    s=list(map(int,input().split()))
    if k>min(s[1:]):
        l.append(s[0])
print (len(l))
for i in sorted(l):
    print (i,end=" ")
