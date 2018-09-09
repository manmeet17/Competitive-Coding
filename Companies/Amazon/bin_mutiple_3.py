for _ in range(int(input())):
    n=input()
    k=len(n)
    o=0
    e=0
    for i in range(k):
        if i%2==0 and n[k-i-1]=='1':
            o+=1
        elif n[k-i-1]=='1':
            e+=1
    print (1 if abs(o-e)%3==0 else 0)
