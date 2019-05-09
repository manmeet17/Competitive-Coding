for _ in range(int(input())):
    s=input()
    l=[]
    n=int(input())
    for i in range(n):
        l.append(input())
    xor=0
    for i in l:
        xor^=s.count(i)
    print ("Teddy" if xor else "Tracy")