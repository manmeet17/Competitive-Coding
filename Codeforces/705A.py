n=int(input())
s="that"
h="I hate "
l="I love "
k=""
for i in range(1,n+1):
    if(i!=n):
        if(i==1 or i%2!=0):
            print (h+s,end=" ")
        else:
            print (l+s,end=" ")
    else:
        if(i==1 or i%2!=0):
            print (h+"it")
        else:
            print (l+"it")
