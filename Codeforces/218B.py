n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,l))
mi=ma=0
for i in range(n):
    k=max(l)
    ma+=k
    l[l.index(k)]-=1
for i in range(n):
    k=min(p)
    if(k==0):
        p.remove(0)
    k=min(p)
    mi+=k
    p[p.index(k)]-=1
print (ma,mi)
