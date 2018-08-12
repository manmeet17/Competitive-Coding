def findW(l,x):
    for k in range(len(l)):
        if(len(l[k])==2):
            if(l[k][0]==x or l[k][1]==x):
                return k
        else:
            if(l[k][0]==x):
                return k
    return -1


for i in range(int(input())):
    a=list(input())
    b=list(input())
    f=0
    l=[]
    for x,y in zip(a,b):
        l.append(list(set([x,y])))
    l=sorted(l,key = lambda x: len(x))
    s="bob"
    for j in s:
        t=(findW(l,j))
        if(t!=-1):
            l.pop(t)
        else:
            f=1
            break
    print ("yes" if f!=1 else "no")
