for i in range(int(input())):
	t=["C","E","S"]
	m=[0]*3
	k=False
	s=list(input())
	for j in range(len(s)):
		if s[j]=="C":
			if (m[1]==0 and m[2]==0):
				m[0]=1
			else:
				k=True
				break
		elif s[j]=="E":
			if (m[0]==1 and m[2]==0) or (m[0]==0 and m[2]==0):
				m[1]=1
			else:
				k=True
				break
		elif s[j]=="S":
			if (m[0]==1 and m[1]==1) or (m[0]==0 and m[1]==0) or (m[0]==1 and m[1]==0) or (m[0]==0 and m[1]==1):
				m[2]=1
			else:
				k=True
				break
	if k==True:
		print ("no")
	else:
		print ("yes")
