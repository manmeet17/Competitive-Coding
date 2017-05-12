s=input()
k=[0]*4
p=[0]*4
l=[]
for i in range(0,len(s),4):
    l.append(s[i:i+4])
for i in l:
    if 0 not in k:
        break
    for j in range(len(i)):
        if(i[j]!='!'):
            k[j]=i[j]
for i in range(len(s)):
    if(s[i]=="!"):
        p[i%4]+=1
print (p[k.index('R')],p[k.index('B')],p[k.index('Y')],p[k.index('G')])
