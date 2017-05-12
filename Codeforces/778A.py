s=list(input())
p=input()
i=0
l=list(map(int,input().split()))
while(True):
    del(s[l[i]])
    k=''.join(s)
    if p not in k:
        print (i)
        break
    i+=1
    
