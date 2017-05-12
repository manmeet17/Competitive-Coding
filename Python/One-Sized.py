for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    while(len(s)!=0 or len(s)!=1):
        m=s.index(min(s))+1
        for i in range(len(s)):
            s[i]-=m
            l.append(s[i])
        s=list(set(s)-set(l))
    if(len(s)==0):
        print ("Kushagra")
    else:
        print ("Ladia")
                
