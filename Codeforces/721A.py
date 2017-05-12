n=int(input())
s=input()
c=k=0
l=[]
for i in range(n):
    if(s[i]=="B"):
        c+=1
        if(i==n-1):
            l.append(c)
            k+=1
    elif(s[i]=="W" and i!=0 and c!=0):
        l.append(c)
        c=0
        k+=1
if(k==0):
    print (0)
else:
    print (k)
    for i in l:
        print (i,end=" ")
