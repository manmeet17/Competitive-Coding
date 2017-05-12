for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    if l[1]!=l[0]+1:
        print (l[0])
        continue
    for j in range(1,n):
        if l[j]!=l[j-1]+1:
            f=True
            print (l[j])
        
    
