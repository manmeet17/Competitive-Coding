from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    l=input().split()
    q=[]
    d=defaultdict(int)
    for i in range(n):
        d[l[i]]+=1
        q.append(l[i])
        while len(q)>0:
            if d[q[0]]>1:
                q.pop(0)
            else:
                print (q[0],end=' ')
                break
        if len(q)==0:
            print ("-1",end=' ')
    print()
