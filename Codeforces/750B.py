l=[]
for i in range(int(input())):
    l.append(input().split())
s=0
f=0
for i in range(len(l)):
    if(s==20000):
        if(l[i][1]!="North"):
            print ("NO")
            f=1
            break
    elif(s==0):
        if(l[i][1]!="South"):
            print ("NO")
            f=1
            break
    if(l[i][1]=="South"):
        s+=int(l[i][0])
    elif(l[i][1]=="North"):
        s-=int(l[i][0])
if(f==0):
    if(s==0):
        print ("YES")
    else:
        print ("NO")
