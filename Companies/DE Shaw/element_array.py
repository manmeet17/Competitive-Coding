t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for j in range(0,n,2):
        if(j!=n-1):
            print ("J val; ",j)
            if(l[j]!=l[j+1]):
                f=1
                print (l[j])
        elif j==n-1 and f==0:
            print (l[j])
