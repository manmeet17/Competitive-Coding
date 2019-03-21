def build(segment, l, n):
    ans=n
    for i in range(n):
        segment[i+n][l[i]]=1
    
    for i in range(n-1,0,-1):
        odd=0
        f=1
        for k in segment[2*i].keys():
            if k not in segment[i]:
                segment[i][k]=0
            segment[i][k]+=segment[2*i][k]
        for k in segment[2*i+1].keys():
            if k not in segment[i]:
                segment[i][k]=0
            segment[i][k]+=segment[2*i+1][k]
            if segment[i][k]%2!=0:
                odd+=1
            if odd>1:
                f=0
                break
        if f==1:
            ans+=1
    print(ans)
    
for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(int(input()))
    segment= [dict() for x in range(2*n)]
    build(segment,l,n)