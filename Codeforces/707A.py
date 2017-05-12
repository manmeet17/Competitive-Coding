n,m=list(map(int,input().split()))
for i in range(n):
    s=input().split()
    for j in s:
        if(j!="W" or j!="B" or j!="G"):
            print ("#Color")
            d=True
            break
    if(d==True):
        break
if(d==False):
    print ("#Black&White")
