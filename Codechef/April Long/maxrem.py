n=int(input())
l=list(sorted(set(map(int,input().split()))))
if len(l)==1:
    print(0)
else:
    print(l[-2])