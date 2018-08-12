p,s=list(map(int,input().split()))
df={}
for i in range(p):
    s=list(map(int,input().split()))
    n=list(map(int,input().split()))
    l=[(a,b) for a,b in zip(s,n)]
    l=sorted(l,key=lambda x: x[0])
    c=0
    for j in range(len(l)-1):
        if(l[j+1][1]<l[j][1]):
            c+=1
    df[i]=c
# diffs=df.values()
print (df)
x=sorted(df, key=lambda k: (df[k],-k))
print (x)
for i in x:
    print (i+1)
# for i in range(len(x)-1):
#     if(x[i][1]==x[i+1][1])
