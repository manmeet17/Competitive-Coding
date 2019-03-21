n,m=map(int,input().split())
c=0
if m%n==0:
    m/=n
    while m%6==0:
        m/=6
        c+=2
    while m%3==0:
        m/=3
        c+=1
    while m%2==0:
        m/=2
        c+=1
    if m==1:
        print(c)
    else:
        print(-1)
else:
    print(-1)