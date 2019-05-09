def seive(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    return prime


l=[]
m=-1
for _ in range(int(input())):
    n=int(input())
    l.append(n)
    m=max(m,n)
prime=seive(m)
d={}
c=0
for i, val in enumerate(prime[2:],2):
    if val==True:
        c+=1
    d[i]=c
# print(d)
for n in l:
    if n==1:
        print("Bob")
        continue 
    # print(n,d[n])
    if d[n]&1==1: 
        print("Alice")
    else:
        print("Bob")
