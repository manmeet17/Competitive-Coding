from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
checker=l[:]
d=defaultdict(int)
d[0]=0
d[l[0]]=1
for i in range(1,n-1):
    l[i]+=l[i-1]
    d[l[i]]=i+1
x=list(sorted(d.items(),key= lambda x: x[0]))
ans=[0]*n
c=1
for i in x:
    ans[i[1]]=c
    c+=1
def check(ans,l):
    for i in range(1,n):
        if checker[i-1]!=(ans[i]-ans[i-1]):
            return [-1]
    return ans

print(*check(ans,l))