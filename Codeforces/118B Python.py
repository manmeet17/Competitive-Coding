n=int(input())
l=list(range(n))+list(range(n+1))[::-1]
for i in l:
    s=[" "]*(n-i)+list(map(str,range(i)))+list(map(str,range(i+1)))[::-1]
    print (" ".join(s))
    
