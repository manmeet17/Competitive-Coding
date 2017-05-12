n=int(input())
s=list(map(int,input().split()))
for i in range(n):
    s[i]=(s[i],i+1)
s.sort()
for i in range(n//2):
    print (s[i][1],s[n-i-1][1])
