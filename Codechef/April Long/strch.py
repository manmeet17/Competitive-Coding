for _ in range(int(input())):
    n=int(input())
    s,x = input().split()
    c=[0]*n
    tot=0
    last=-1
    for i in range(n):
        c[i]=(i+1)*(i+2)//2
    for i in range(n):
        if s[i]==x:
            last=i
            if i!=0:
                tot+=c[i]-c[i-1]
            else:
                tot+=1
        elif last!=-1:
            tot+=c[i]-c[i-1]-(i-last)
    print(tot)
