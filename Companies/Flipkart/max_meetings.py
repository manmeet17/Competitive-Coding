for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    l=[]
    c=0
    for i,j in zip(s,f):
        l.append((i,j,c))
        c+=1
    l=sorted(l,key=lambda x:(x[1]))
    # print(l)
    ans=[l[0]]
    cur=ans[0]
    for i in range(1,n):
        if l[i][0]>cur[1]:
            ans.append(l[i])
            cur=l[i]
    for i in ans:
        print(i[2]+1,end=' ')
    print()