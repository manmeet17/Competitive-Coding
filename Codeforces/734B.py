a,b,c,d=list(map(int,input().split()))
f=min(a,c,d)
print (f*256+min(a-f,b)*32)
