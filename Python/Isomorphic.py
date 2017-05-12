t=int(input())
num=input()
l=list()
for i in range(t-1):
	d={}
	n=input()
	p=False
	if len(n)!=len(num):
		continue
	else:
		for j in range(len(num)):
			if num[j] not in d:
				d[num[j]]=n[j]
			else:
				if n[j]!=d[num[j]]:
					p=True
					break
		if(p==False):
			l.append(n)
if(len(l)==0):
	print ("No isomorphic")
else:
	print (num)
	for i in l:
		print (i)