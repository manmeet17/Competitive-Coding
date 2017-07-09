n=int(input())
l=(input().split(" "))
l=("".join(l)).split("1")
t=hit=cur=0
for i in range(len(l)):
    if l[i]!='':
        t+=len(l[i])
    else:
        t+=1
        if(hit>0):
            if(t>=cur):
                cur=t
            hit=0
        hit=1
