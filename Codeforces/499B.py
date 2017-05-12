n,k=map(int,input().split())
for i in range(n):
    s=list(map(int,input().split()))
    if k>min(s[1:]):
        l.append(s[0])
print (len(l))
print (sorted(l))
        
