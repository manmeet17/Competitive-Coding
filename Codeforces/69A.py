x=y=z=0
for i in range(int(input())):
    s=list(map(int,input().split()))
    x+=s[0]
    y+=s[1]
    z+=s[2]
if(x==0 and y==0 and z==0):
    print ("YES")
else:
    print ("NO")
