class Solution:
    def addDict(self,dp,val):
        if val in dp:
            dp[val]+=1
        else:
            dp[val]=1
        return dp
    
    
    def postOrder(self,root,dp):
        if not root:
            return (0,dp)
        else:
            if not root.left and not root.right:
                dp=self.addDict(dp,root.val)
                return (root.val,dp)
            lsum=self.postOrder(root.left,dp)[0]
            rsum=self.postOrder(root.right,dp)[0]
            dp=self.addDict(dp,root.val+lsum+rsum)
            return (root.val+lsum+rsum,dp)
            
    
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dp=dict()
        dp=self.postOrder(root,dp)[1]
        t=max(dp.values())
        ans=[]
        for i in dp.keys():
            if(dp[i]==t):
                ans.append(i)
        return ans
