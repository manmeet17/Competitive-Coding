class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r={}
        c={}
        n=len(matrix)
        if n!=0:
            m=len(matrix[0])
            for i in range(n):
                for j in range(m):
                    if i not in r or j not in c:
                        if matrix[i][j]==0:
                            r[i]=1
                            c[j]=1
            for i in r.keys():
                matrix[i]=[0]*m
            for j in c.keys():
                for k in range(n):
                    matrix[k][j]=0
