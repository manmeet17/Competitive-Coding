s,k=input().split()
s=list(s)
p=len(s)
k=int(k)
if p<=k:
    print (p-1)
else:
    t=0
    j=p-1
    while(k!=0 and j!=-1):
        if s[j]!='0':
            t+=1
        else:
            k-=1
        j-=1
    if j==-1:
        print (p-1)
    else:
        print (t)
