import heapq
for _ in range(int(input())):
    n,a,b,x,y,z=map(int,input().split())
    l=list(map(int,input().split()))
    # dpp=(z-a)//x
    dho=(z-b)//y
    # if dpp<dho:
    #     print(0)
    #     continue
    a+=dho*x
    l=[-x for x in l]
    heapq.heapify(l)
    f=0
    c=0
    while a<z:
        k=abs(heapq.heappop(l))
        if k==0:
            break
        a+=k
        c+=1
        heapq.heappush(l,-(k//2))
        # print(list(l),a,c)
    if a<z:
        print("RIP")
    else:
        print(c)