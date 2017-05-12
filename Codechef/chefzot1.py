n=int(input())
l=input()
n=l.split(" 0")
m=sorted(n,key=lambda x:len(x),reverse=True)
print (m)
if "0" in m[0]:
    print (len(m[0].split())-1)
else:
    print (len(m[0].split()))
