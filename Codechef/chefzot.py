n=int(input())
l=list(map(int,input().split()))
j=ans=0
for i in range(n):
    m=l[i]
    if m==0 or i==n-1:
        k=i-j
        if i==n-1:
            k=i-j+1
        if k>ans:
            ans=k
        j=i+1
print (ans)
