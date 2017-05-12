w=b=0
d={'r':5,'n':3,'b':3,'p':1,'k':0,'q':9}
for i in range(8):
    s=input()
    for j in s:
        if j=='.':
            continue
        if j.isupper():
            w+=d[j.lower()]
        else:
            b+=d[j]
if w>b:
    print ("White")
elif w<b:
    print ("Black")
else:
    print ("Draw")
