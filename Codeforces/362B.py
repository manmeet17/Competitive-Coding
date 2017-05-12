import sys
n,d=list(map(int,input().split()))
if(d==0):
    print ("YES")
    sys.exit(0)
l=sorted(list(map(int,input().split())))
flag=0
if(l[0]==1 or l[-1]==n):
    print ("NO")
else:
    for i in range(d-2):
        if l[i+1]==l[i]+1 and l[i+2]==l[i]+2:
            print ("NO")
            flag=1
            break
    if(flag==0):
        print ("YES")
    
