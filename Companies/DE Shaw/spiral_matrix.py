class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m=len(matrix)
        if m==0:
            return []
        if m==1:
            return matrix[0]
        n=len(matrix[0])
        down=m-1
        right=n-1
        left=0
        up=0
        i=0
        j=0
        d="r"
        l=[]
        dp=[[0 for _ in range(n)] for _ in range(m)]
        # print(di)
        while(up<=down and left<=right):
            # if dp[i][j]==1:
            #     break
            if d=="r":
                l.append(matrix[i][j])
                # print ("R---->",l,i,j)
                dp[i][j]=1
                if j==right:
                    d='d'
                    i+=1
                    up+=1
                    continue
                j+=1
            elif d=="d":
                l.append(matrix[i][j])
                # print ("D---->",l,i,j)
                # if i==up and right==j:
                #     break
                dp[i][j]=1
                if i==down:
                    d='l'
                    j-=1
                    right-=1
                    continue
                i+=1
            elif d=="l":
                l.append(matrix[i][j])
                # print ("L---->",l,i,j)
                # if i==up and right==j:
                #     break
                dp[i][j]=1
                if j==left:
                    d='u'
                    i-=1
                    down-=1
                    continue
                j-=1
            elif d=="u":
                l.append(matrix[i][j])
                # print ("U---->",l,i,j)
                # if i==up and right==j:
                #     break
                dp[i][j]=1
                if i==up:
                    d='r'
                    j+=1
                    left+=1
                    continue
                i-=1
        return l
