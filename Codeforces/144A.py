n=int(input())
time=0
s=list(map(int,input().split()))
man=s.index(max(s))
minx=len(s)-s[::-1].index(min(s)) - 1
if(minx!=len(s)-1):
    if(minx<man):
        man-=1
    time+=len(s)-1-minx
if(man!=0):
    time+=man
print (time)
