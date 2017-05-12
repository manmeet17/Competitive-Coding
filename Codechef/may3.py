for i in range(int(input())):
	n=int(input())
	l=sorted(list(map(int,input().split())))
	m=l[n:]
	print (m[n//2])
	m=[]
	for j in range(n):
		m.append(l[j])
		m.append(l[n*2-j-1])
	for j in m:
		print (j,end=" ")
	print ()