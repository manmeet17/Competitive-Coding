d=[1,2,5,10,20, 50, 100, 500, 1000]

def findMin(n,d):
    for i in range(len(d)):
        if n//d[i]<1:
            return (d[i-1],n//d[i-1])
    return (d[-1],n//d[-1])

for _ in range(int(input())):
    n=int(input())
    s=""
    while(n):
        rem=findMin(n,d)
        s+=(str(rem[0])+" ")*rem[1]
        n-=rem[0]*rem[1]
    print(s)
    
