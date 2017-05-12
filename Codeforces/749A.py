n=int(input())
print (n//2)
s="2 "
if(n%2==0):
    print (s*(n//2))
else:
    print (s*((n-3)//2) + "3")
