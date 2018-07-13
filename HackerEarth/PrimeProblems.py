import sys
f=[]
def solve(n):
    for i in range(n,0,-1):
        t=False
        for j in range(2,i):
            if(i%j==0):
                t=True
                break
        if(t==False):
            return i
s=t=0
n=int(input())
l=list(map(int,input().split()))
if(n==1):
    print (0)
    sys.exit(0)
while(n>1):
    k=solve(n)
    # print ("k:",k)
    s+=sum(l[t:t+k])
    n-=k
    t+=k
print (s)
