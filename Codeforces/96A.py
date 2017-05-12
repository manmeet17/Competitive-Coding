s=input()
a=b=t=0
for i in s:
    if i=="0":
        a+=1
        b=0
    else:
        b+=1
        a=0
    if(a>=7 or b>=7):
        print ("YES")
        t=1
        break
if t==0:
    print ("NO")
