'''
codeforces
dodivthree
12345678910
7 8
4 9
2 2
9 10
3 1
'''
from collections import Counter, defaultdict
from itertools import chain
n=int(input())
l=list(input())
r=list(input())
a=defaultdict(list)
b=defaultdict(list)
for i in enumerate(l,1):
    a[i[1]].append(i[0])
for i in enumerate(r,1):
    b[i[1]].append(i[0])
# print(a)
# print(b)
aq=[]
ar=[]
bq=[]
br=[]
ans=[]
tot=0
for i in a:
    if i=='?':
        aq.extend(a[i])
        continue
    if i in b:
        la=len(a[i])
        lb=len(b[i])
        while la>=1 and lb>=1:
            ans.append((a[i].pop(0), b[i].pop(0)))
            la-=1
            lb-=1
            tot+=1
    ar.extend(a[i])
# for i in b:
#     if i=="?":
#         bq.extend(b[i])
#     else:
#         br.extend(b[i])
# print(tot,*ans)
# print("A-->",ar)
# print("A?-->",aq)
# print(tot,ans)
bq=[]
if '?' in b:
    bq=b.pop('?')
br=list(chain(*list(b.values())))
# print("B-->",br)
# print("B?-->",bq)
laq=len(aq)
lar=len(ar)
lbr=len(br)
lbq=len(bq)

while laq>0 and lbr>0:
    ans.append((aq.pop(0), br.pop(0)))
    laq-=1
    lbr-=1
    tot+=1
# print(tot,ans)


while lbq>0 and lar>0:
    ans.append((ar.pop(0), bq.pop(0)))
    lbq-=1
    lar-=1
    tot+=1
# print(tot,ans)

while laq>0 and lbq>0:
    ans.append((aq.pop(0), bq.pop(0)))
    laq-=1
    lbq-=1
    tot+=1
# print(tot,ans)
print(tot)
for i in ans:
    print(i[0],i[1])
