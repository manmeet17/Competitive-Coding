from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    s=input().split()
    d=defaultdict(int)
    q=[]
    fin=[]
    f=0
    for i in range(n):
        if s[i] not in d:
            q.append(s[i])
            d[s[i]]+=1
            fin.append(q[f])
        elif s[i] in d and s[i]!=q[f]:
            d[s[i]]+=1
            fin.append(q[f])
        else:
            d[s[i]]+=1
            # print("jambamjoo")
            while d[q[f]]>1:
                f+=1
                if f>len(q)-1:
                    break
            if f>len(q)-1:
                fin.append(-1)
            else:
                fin.append(q[f])
        print("Curr---->",s[i])
        print ("Q--->",q)
        print("F val--->",f)
        print("Fin--->",fin)
        print("D---->",d)
        print("\n\n")