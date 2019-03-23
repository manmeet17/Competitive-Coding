def solve(s,n):
    c=0
    for i in range(n):
        if int(s[i])%2==0:
            c+=i+1
    return c

n=int(input())
s=input()
print(solve(s,n))
