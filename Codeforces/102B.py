n=list(map(int,input()))
i=0
while(len(n)!=1):
    n=list(map(int,str(sum(n))))
    i+=1
print (i)
