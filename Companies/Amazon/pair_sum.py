from collections import defaultdict
for _ in range(int(input())):
    n,m,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    da=defaultdict(int)
    db=defaultdict(int)
    for i in b:
        db[i]+=1
    ans=[]
    for i in a:
        if x-i in db:
            for j in range(db[x-i]):
                ans.append((i,x-i))
    k=len(ans)
    ans=sorted(ans)
    for i in range(k):
        if i!=k-1:
            print (str(ans[i][0])+' '+str(ans[i][1]),end=', ')
        else:
            print (str(ans[i][0])+' '+str(ans[i][1]))
    if k==0:
        print (-1)
