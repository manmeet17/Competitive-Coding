n=int(input())
l=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if(i==0 or j==0):
            l[i][j]+=1
        else:
            l[i][j]+=l[i-1][j]+l[i][j-1]
print (l[n-1][n-1])
                
