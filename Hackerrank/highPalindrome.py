# def solve(l,n):
#     c=0
#     mark=[0]*n
#     for i in range(0,n//2):
#         if l[i]!=l[n-i-1]:
#             prev=l[i]
#             new=l[n-i-1]
#             l[i],l[n-i-1]=[max(l[i],l[n-i-1])]*2
#             if prev!=l[i]:
#                 mark[i]=1
#             if new!=l[n-i-1]:
#                 mark[n-i-1]=1
#             c+=1
#         if c>k:
#             return -1
#     # print('Here c-->',c,l)
#     if c==k:
#         return ''.join(l)
#     # print(mark,l,c)
#     prec=c
#     for i in range(0,n//2+1):
#         pre=l[:]
#         # print("Check--->",i,l,c)
#         inc=2
#         if i==n-i-1:
#             inc=1
#         if l[i]!='9':
#             l[i],l[n-i-1]=['9']*2
#             c=c-(mark[i]-mark[n-i-1])+inc
#             # print("Ans",l,c)
#         if c>k:
#             if prec<k and n%2!=0:
#                 pre[n//2]='9'
#                 prec+=1
#             return ''.join(pre)
#         if c==k:
#             return ''.join(l)
#         prec=c
#     return ''.join(l)


def solve(v,n):
    c=0
    rep=set()
    h=n//2
    for i in range(h):
        l,r=v[i],v[n-i-1]
        if l!=r:
            v[i]=v[n-i-1]=max(l,r)
            rep.add(i)
            c+=1
    if c>k: return -1
    for i in range(h):
        inc=1 if i in rep else 2
        if v[i]!='9' and c+inc<=k:
            v[i]=v[n-i-1]='9'
            c+=inc
    if n%2 and c<k: v[h]='9'
    return ''.join(v)
            


n,k=map(int,input().split())
curr=input()
s=list(curr)
curr=int(curr)
print(solve(s,n))