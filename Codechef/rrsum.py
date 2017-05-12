n,t=list(map(int,input().split()))
for i in range(t):
    c=0
    p=int(input())
    if p>=n+2 and p<=3*n:
        if p<(4*n+2)//2:
            print (p-n-1)
        elif p>(2*n+1):
            print (n-(p-2*n)+1)
        else:
            print (n)
    else:
        print (0)
