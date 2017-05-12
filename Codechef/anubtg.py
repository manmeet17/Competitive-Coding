for i in range(int(input())):
    n=int(input())
    s=0
    l=sorted(list(map(int,input().split())),reverse=True)
    p=[]
    for j in range(0,n):
        p=l[j:j+4]
        if len(p)>=2:
            s+=p[0]+p[1]
        else:
            s+=p[0]
    print (s)
