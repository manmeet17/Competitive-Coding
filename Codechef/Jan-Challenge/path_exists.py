def dfs(grid,i,j,n,s):
    if grid[i][j]==2:
        print(True,i,j)
        return True
    a=b=c=d=False
    print(i,j,s)
    if i+1<n and  grid[i+1][j]!=0 and (i+1,j) not in s:
        s.add((i+1,j))
        a=dfs(grid,i+1,j,n,s)
        
    if i-1>=0 and grid[i-1][j]!=0 and (i-1,j) not in s:
        s.add((i-1,j))
        b=dfs(grid,i-1,j,n,s)
        
    if j+1<n and grid[i][j+1]!=0 and (i,j+1) not in s:
        s.add((i,j+1))
        c=dfs(grid,i,j+1,n,s)
        
    if j-1>=0 and grid[i][j-1]!=0 and (i,j-1) not in s:
        s.add((i,j-1))
        d=dfs(grid,i,j-1,n,s)
    return a or b or c or d

        

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    grid=[]
    for j in range(0,n*n,n):
        grid.append(l[j:j+n])
    print (grid)
    s=set()
    f=0
    for j in range(n):
        for k in range(n):
            if grid[j][k]==1:
                s.add((j,k))
                print(dfs(grid,j,k,n,s))
                f=1
                break
        if f==1:
            break
    print (j,k)
    