for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    f=0
    for j in s:
        if j==0:
            f+=1000+100
        elif j==1 and s!=0:
            f+=100
