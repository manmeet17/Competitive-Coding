from collections import defaultdict as dd

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    # l=[]
    tot=0
    d=dd(list)
    # mat=[[0 for i in range(m)] for j in range(n)]
    for i in range(k):
        x,y=map(int,input().split())
        # l.append([x,y])
        d[x].append(y)
        # mat[x-1][y-1]=1
    # l=sorted(l)
    # print(l)

    for i,j in d.items():
        for k in j:
            if k-1 not in j:
                tot+=1
            # print(tot)
            if k+1 not in j:
                tot+=1
            # print(tot)            
            if i==1 or (i-1 not in d) or ((k not in d[i-1])):
                tot+=1
            # print(tot)            
            if i==n or (i+1 not in d) or ((k not in d[i+1])):
                tot+=1
        # print(i,j, tot)
    print(tot)