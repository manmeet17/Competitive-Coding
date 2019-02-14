for _ in range(int(input())):
    n=int(input())
    ans=set()
    for i in range(n):
        s=set(input())
        if i==0:
            ans=s
        else:
            ans.intersection_update(s)
        # print(s,ans)
    print (len(ans))
