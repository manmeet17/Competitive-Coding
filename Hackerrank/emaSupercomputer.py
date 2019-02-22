def twoPluses(grid,n,m):
    ans=[]
    for i in range(n):
        for j in range(m):
            if grid[i][j]!="B":
                ans.append(getRect(grid,i,j,n,m))
    return sorted(ans)

def isSafe(grid,i,j,n,m):
    if i>=0 and j>=0 and i<n and j<m and grid[i][j]!="B":
        return True
    return False
               
def getRect(grid,i,j,n,m):
    c=[0]*4
    b=j+1
    a=i
    while isSafe(grid,a,b,n,m):
        c[0]+=1
        b+=1
    b=j
    a=i+1
    while isSafe(grid,a,b,n,m):
        c[1]+=1
        a+=1
    b=j-1
    a=i
    while isSafe(grid,a,b,n,m):
        c[2]+=1
        b-=1
    b=j
    a=i-1
    while isSafe(grid,a,b,n,m):
        c[3]+=1
        a-=1
    if 0 not in c:
        return 1+min(c)*4
    # print(i,j)
    return 1



if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = twoPluses(grid,n,m)
    if len(result)==0:
        print(0)
    else:
        print(result)
        print(result[-1]*result[-2])