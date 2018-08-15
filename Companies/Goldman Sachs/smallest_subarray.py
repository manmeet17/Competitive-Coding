for i in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    s=l[0]
    p=0
    m=0
    if(n==1):
        print (1 if s>x else 0)
        continue
    val=10000007
    for j in range(1,n):
        s+=l[j]
        m+=1
        while(s>x):
            val=min(val,m-p+1)
            s-=l[p]
            p+=1
    print (val)
    	
