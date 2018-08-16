for j in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    for i in range(0,n-1,2):
        l[i+1],l[i]=l[i],l[i+1]
    for i in l:
        print (i,end=' ')
    print()
