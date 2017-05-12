a,b,c=map(int,raw_input().split())
print min(2*min(a+b,b+c,a+c),a+b+c)
