for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    t=x=0
    for j in range(n-1):
        x+=l[-1]-l[j]
    print(x)
    if len(set(l))==1:
        print (t)
        continue
        

