n=int(input())
av=cop=res=0
s=list(map(int,input().split()))
for i in s:
    if(i>0):
        cop+=i
    else:
        if(cop>0):
            cop-=1
        else:
            res+=1
print (res)
