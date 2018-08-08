# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root,s,k,path):
            if not root:
                return
            s+=root.val
            path.append(root.val)
            if(s==k and root.left==None and root.right==None):
                self.res.append(path[:])
            else:
                if root.left:
                    dfs(root.left,s,k,path)
                if root.right:
                    dfs(root.right,s,k,path)
            path.pop()
        dfs(root,0,sum,[])
        return self.res
