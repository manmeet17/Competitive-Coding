def build(l,n):
    segment=[0]*2*n

    for i in range(n):
        segment[i+n]=l[i]
    
    for i in range(n-1,0,-1):
        segment[i]=min(segment[i<<1], segment[i<<1 | 1])
    
    return segment

def query(x,y,seg):
    x+=n
    y+=n
    m=float("inf")
    while x<y:
        # print(x,y)
        if x&1:
            m=min(m,seg[x])
            x+=1
        if y&1:
            y-=1
            m=min(m,seg[y])
        
        x>>=1
        y>>=1
    return m


n=int(input())
l=list(map(int,input().split()))
seg=build(l,n)
# print(seg)
for i in range(int(input())):
    x,y=map(int,input().split())
    print(query(x,y+1,seg))