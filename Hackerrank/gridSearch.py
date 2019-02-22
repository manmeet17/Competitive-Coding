#!/bin/python3

import os


def isSafe(g,p,i,j,R,C,r,c):
    a=0
    for m in range(i,i+r):
        b=0
        for n in range(j,j+c):
            # print(m,n,g[m][n])
            if m>=R or n>=C or g[m][n]!=p[a][b]:
                return False
            b+=1
        a+=1
    return True

    # print(i,j,g[i][j],a,b)
    # if a==r-1 and b==c-1 and g[i][j]==p[a][b]:
    #     print("Found")
    #     return True
    # if (i>=0 and i<R and a>=0 and a<r) and (j<C and b<c and b>=0 and j>=0) and g[i][j]==p[a][b]:
    #     print("Inside--->",i,j,g[i][j],a,b)
    #     return (isSafe(g,p,i+1,j,a+1,b,R,C,r,c) and isSafe(g,p,i,j+1,a,b+1,R,C,r,c))
    
    # if a==r or j==c:
    #     return True
    # return False

# Complete the gridSearch function below.
def gridSearch(G, P, R, C, r ,c):
    for i in range(R):
        for j in range(C):
            if isSafe(G,P,i,j,R,C,r,c):
                return "YES"
            # print("\n")
    return  "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P,R,C,r,c)

        fptr.write(result + '\n')

    fptr.close()

