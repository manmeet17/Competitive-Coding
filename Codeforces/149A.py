import sys
k=int(input())
s=sorted(list(map(int,input().split())),reverse=True)
if(k==0):
    print (0)
else:
    i=0
    gr=0
    t=0
    while(gr<k):
        if(i==12):
            print (-1)
            sys.exit(0)
        gr+=s[i]
        t+=1
        i+=1
    print (t)
