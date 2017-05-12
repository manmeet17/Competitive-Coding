s=sorted(list(map(int,input().split())))
tot=0
for i in s:
    tot+=abs(i-s[1])
print (tot)
