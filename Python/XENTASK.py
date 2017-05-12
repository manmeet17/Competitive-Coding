t=int(input())
for j in range(t):
    n=int(input())
    a=b=0
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    for i in range(n):
        if i%2==0:
            a+=x[i]
            b+=y[i]
        else:
            a+=y[i]
            b+=x[i]
    print (min(a,b))
