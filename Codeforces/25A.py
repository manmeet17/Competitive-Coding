n=int(input())
s=list(map(int,input().split()))
e=o=0
for i in range(3):
    if(s[i]%2==0):
        e+=1
    else:
        o+=1
if(e>o):
    for i in s:
        if(i%2!=0):
            print (s.index(i)+1)
else:
    for i in s:
        if(i%2==0):
            print (s.index(i)+1)
