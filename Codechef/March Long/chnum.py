for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    pos=0
    neg=0
    for j in l:
        if j>0:
            pos+=1
        else:
            neg+=1
    if neg==0:
        print(pos,pos)
    elif pos==0:
        print(neg,neg)
    else:
        print(max(pos,neg),min(pos,neg))