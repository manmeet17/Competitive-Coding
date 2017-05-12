from collections import deque
def lcs(d,p,n):
	c=ma=0
	l=list(d)
	for i in range(n):
		m=l[i:i+p]
		c=m.count(1)
		if c>ma:
			ma=c
	return ma
		
n,k,p=map(int,input().split())
d=deque(list(map(int,input().split())))
dog=input()
for i in dog:
	if i=="!":
		d.rotate(1)
	else:
		print(lcs(d,k,n))