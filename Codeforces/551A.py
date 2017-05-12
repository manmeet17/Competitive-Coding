n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(sorted(l)[::-1].index(i)+1,end=" ")
