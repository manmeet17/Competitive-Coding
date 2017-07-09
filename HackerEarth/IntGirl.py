s=input()
c=0
k=len(s)
t=False
for i in range(k):
    if(int(s[i]) %2==0):
        c+=1
for j in range(k):
    if(int(s[j])%2==0):
        t=True
    if j!=k-1:
        print (c,end=" ")
        if(t):
            c-=1
            t=False
    elif j==k-1:
        print ( 1 if int(s[j])%2==0 else 0)
