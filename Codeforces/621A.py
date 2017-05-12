n=int(input())
s=sorted(list(map(int,input().split())))
k=sum(s)
if(k%2==0):
    print (k)
else:
    for j in s:
        if(j%2!=0):
            break
    print (k-j)
    
