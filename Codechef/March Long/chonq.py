def solve(l,k,n):
    for i in range(n):
        c=1
        s=0
        f=1
        for j in range(i,n):
            s+=l[j]//c
            c+=1
            if s>k:
                f=0
                break
        if f!=0:
            return i+1
    return n+1

for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    print(solve(l,k,n))
    
    