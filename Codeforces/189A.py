n,a,b,c=list(map(int,input().split()))
if((a+b+c)==n):
    print (3)
else:
    if((a+b)==n or (b+c)==n or (a+c)==n):
        print (2)
    else:
        print (1)
