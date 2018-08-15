for i in range(int(input())):
    d={}
    n=int(input())
    s=input().split()
    for j in range(n):
        if s[j] in d:
            d[s[j]]+=1
        else:
            d[s[j]]=1
    l=sorted(list(d.items()),key=lambda x: x[1])
    m=l[-1][1]
    for j in l[::-1]:
        if m!=j[1]:
            print (j[0])
            break
