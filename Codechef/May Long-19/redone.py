# for _ in range(int(input())):
#     n=int(input())
#     l=list(range(1,n+1))
#     for i in range(n-1):
#         x=l.pop()
#         y=l.pop()
#         l.append((x+y+x*y)%1000000007)
#     print(l)

# def factmod(n,p):
#     res=1
#     while n>1:
#         if (n/p)%2==1:
#             res=res*(p-1)
#         res%=p
#         for i in range(2, n%p+1):
#             res=(res*i)%p
#         n/=p
#     return res%p
# prime = [True]*1000001

def preprocess():
    pre=[1]
    n=2
    while n<=1000000:
        pre.append((pre[-1]*n)%1000000007)
        n+=1
    return pre

pre=preprocess()
for _ in range(int(input())):
    n=int(input())
    print((pre[n]-1)%1000000007)
    # print((factmod(n+1, 1000000007)-1)%1000000007)
    # print((calculate_factorial_prime_decompose(n+1)-1)%1000000007)