s=input()
f=0
k="AEIOU"
l=[]
for i in range(len(s)):
    if s[i] in k:
        l.append(i+1-f)
        f=i+1
        p=s[i]
l=l[::-1]
l.append(len(s)-(len(s)-s.index(p)-1))
print (max(l))
