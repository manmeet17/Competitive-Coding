import sys
l=list(map(int,input().split()))
t=False
p=[]
for i in l:
    if(l.count(i)>=4):
        k=i
        t=True
if(t==False):
    print ("Alien")
    sys.exit(0)
for i in l:
    if(i!=k):
        p.append(i)
if(p[0]!=p[1]):
    print ("Bear")
else:
    print ("Elephant")
        
