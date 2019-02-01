def isSafe( maze, x, y,N ): 
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
        return True
    return False
# path=[]

def printSol(sol):
    for i in sol:
        print(i)
    print("\n\n\n")

def paths(arr,x,y,sol,n,s,path):
    if x==n-1 and y==n-1:
        path.append(s)
        return (True,path)
    if isSafe(arr,x,y,n):
        sol[x][y]=1
        # print(x,y,s)
        # printSol(sol)
        if sol[x+1][y]!=1 and paths(arr,x+1,y,sol,n,s+'D',path)[0]:
            sol[x][y]=0
        if sol[x-1][y]!=1 and paths(arr,x-1,y,sol,n,s+'U',path)[0]:
            sol[x][y]=0
        if sol[x][y+1]!=1 and paths(arr,x,y+1,sol,n,s+'R',path)[0]:
            sol[x][y]=0
        if sol[x][y-1]!=1 and paths(arr,x,y-1,sol,n,s+'L',path)[0]:
            sol[x][y]=0
        sol[x][y]=0
        # printSol(sol)

    return (False,path)

def findPath(arr, n):
    # code here
    sol=[[0 for i in range(n+1)] for j in range(n+1)]
    path=[]
    s=""
    p=paths(arr,0,0,sol,n,'',path)
    fin=[]
    for i in p[1]:
        if "LR" not in i and "RL" not in i and "UD" not in i and "DU" not in i:
            fin.append(i)
    for i in sorted(fin):
        s+=i+' '
    return s

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        for i in matrix:
            print(i)
        print(findPath(matrix, n[0]))