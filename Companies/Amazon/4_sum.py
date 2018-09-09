for _ in range(int(input())):
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    f=0
    d={}
    for i in range(n-3):
        for j in range(i+1,n-2):
            a=j+1
            b=n-1
            while(a<b):
                if(l[i]+l[j]+l[a]+l[b]==k):
                    # print (i,j,a,b)
                    f=1
                    ans=str(l[i])+" "+str(l[j])+" "+str(l[a])+" "+str(l[b])+" $"
                    if(ans not in d):
                        d[ans]=1
                        print (ans,end='')
                    a+=1
                    b-=1
                elif (l[i]+l[j]+l[a]+l[b])<k:
                    a+=1
                else:
                    b-=1
    if(f==0):
        print (-1)
        continue
    print()
        
