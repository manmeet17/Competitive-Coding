for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for i in set(l):
        if l.count(i)>n//2:
            print (i)
            f=1
            break
    if f==0:
        print ("NO Majority Element")
