# l=[3,5,7,9,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89]
# for i in range(len(l)):
#     for j in range(len(l)):
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

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    e = []
    ec = 0
    oc = 0
    o = []
    de = {}
    doo = {}
    for i in range(n):
        if l[i] % 2 == 0:
            e.append(l[i])
            ec += 1
            if l[i] not in de:
                de[l[i]] = [i]
            else:
                de[l[i]].append(i)
        else:
            o.append(l[i])
            oc += 1
            if l[i] not in doo:
                doo[l[i]] = [i]
            else:
                doo[l[i]].append(i)
    c = (ec*(ec-1)/2)+(oc*(oc-1)/2)
    t = 0
    for i in range(n):
        if l[i]%2==0:
            if (l[i]^2 in de):
                for j in de[l[i]^2]:
                    if j>i:
                        t+=1
            if (l[i]^4 in de):
                for j in de[l[i]^4]:
                    if j>i:
                        t+=1
            if (l[i]^0 in de):
                for j in de[l[i]^0]:
                    if j>i:
                        t+=1
        else:
            if (l[i]^2 in doo):
                for j in doo[l[i]^2]:
                    if j>i:
                        t+=1
            if (l[i]^4 in doo):
                for j in doo[l[i]^4]:
                    if j>i:
                        t+=1
            if (l[i]^0 in doo):
                for j in doo[l[i]^0]:
                    if j>i:
                        t+=1
    print(int(c-t))
