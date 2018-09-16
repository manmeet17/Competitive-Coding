d={}
for i in range(1,27):
    d[i]=chr(i+64)

def helper(data,k):
    if k==0:
        return 1
    s=len(data)-k
    if data[s]=="0":
        return 0
    result=helper(data,k-1)
    if k>=2 and int(data[s:s+2]) in d:
        result+=helper(data,k-2)
    return result
    
for _ in range(int(input())):
    n=int(input())
    s=input()
    print(helper(s,len(s)))
