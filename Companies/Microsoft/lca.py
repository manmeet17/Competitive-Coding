# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self,root,p,q):
        if root==None:
            return False
        l=self.find(root.left,p,q)
        r=self.find(root.right,p,q)
        if (root.val==q.val or root.val==p.val) and (l or r):
            return root
        if (root.val==q.val or root.val==p.val):
            return root
        
        if l and r:
            return root
        
        return (l or r)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return(self.find(root,p,q))
