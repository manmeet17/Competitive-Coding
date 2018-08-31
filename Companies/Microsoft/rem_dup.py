from collections import defaultdict
for i in range(int(input())):
    s=input()
    d=defaultdict(int)
    f=""
    for j in s:
        if(j not in d):
            f+=j
        d[j]+=1
    print (f)
