import bisect
input()
a=sorted(list(map(int,input().split())),key=int)
for i in range(int(input())):
	print(bisect.bisect(a,int(input())))
