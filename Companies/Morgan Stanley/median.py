a=[]
n=int(input())
for i in range(n):
    s=int(input())
    a.append(s)
    a.sort()
    if(i%2==0):
        print (a[i//2])
    else:
        print ((a[(i+1)//2]+a[(i-1)//2])//2)
