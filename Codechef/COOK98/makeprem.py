for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        if abs(l[i])-1<n:
            l[abs(l[i])-1]=-abs(l[abs(l[i])-1])
        # print("L---->",l,i,l[i])
    x=0
    for i in l:
        if i>0:
            x+=1
    print(x)
