n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if (i==0 or i==n-1):
        if(i==0):
            print (l[1]-l[0],l[-1]-l[0])
        else:
            print (l[-1]-l[-2],l[-1]-l[0])
    else:
        print (min(l[i]-l[i-1],l[i+1]-l[i]),max(l[i]-l[0],l[-1]-l[i]))
