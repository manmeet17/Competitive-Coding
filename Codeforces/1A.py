n=int(input())
time=0
s=list(map(int,input().split()))
man=s.index(max(s))
if(s[-1]!=min(s)):
    if(s.index(min(s))<s.index(max(s))):
        man-=1
    time+=len(s)-1-s.index(min(s))
if(man!=0):
    time+=man
print (time)
