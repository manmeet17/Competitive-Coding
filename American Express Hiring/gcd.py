'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

import math

n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
s=0
for i in range(0,n):
    a=l[i:i+k]
    print(a)
    if(len(a)==k):
        if(k>=2):
            gcd=a[0]
            for j in range(1,k):
                gcd=math.gcd(gcd,a[j])
            s+=sum(a)*gcd
            print(gcd,s)
        else:
            s+=sum(a)*l[i]
print(s)
