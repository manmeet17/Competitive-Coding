# l=[3,5,7,9,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89]
# for i in range(len(l)):
#      range(len(l)):
#         print (l[i]+l[j],end=' ')
#     print()


# l=list(range(2,50,2))
# for i in range(len(l)):
#     print (l[i],end=' ')
# print("\n")

# for i in range(len(l)):
#     print (l[i],end='   ')
#     for j in range(len(l)):
#         print (l[i]^l[j],end=' ')
#     print()

from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    e = []
    ec = 0
    oc = 0
    o = []
    de = defaultdict(int)
    doo = defaultdict(int)
    for i in range(n):
        if l[i] % 2 == 0:
            e.append(l[i])
            ec += 1
            de[l[i]]+=1
        else:
            o.append(l[i])
            oc += 1
            doo[l[i]]+=1
    c = (ec*(ec-1)/2)+(oc*(oc-1)/2)
    t = 0
    # print(de,doo,c)
    for i in range(n):
        # print(l[i],t)
        if l[i]%2==0:
            if (l[i]^2 in de):
                t+=de[l[i]^2]
            if (l[i]^0 in de):
                t+=de[l[i]^0]-1
        else:
            if (l[i]^2 in doo):
                t+=doo[l[i]^2]
            if (l[i]^0 in doo):
                t+=doo[l[i]^0]-1
    print(int(c-t//2))
