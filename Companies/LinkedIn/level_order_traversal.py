# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans=[]
        l=[]
        def level(root,l,ans):
            queue=[root,None]
            while len(queue)>0:
                r=queue.pop(0)
                if r is not None:
                    l.append(r.val)
                    if(r.left is not None):
                        queue.append(r.left)
                    if(r.right is not None):
                        queue.append(r.right)
                else:
                    if len(queue)>0:
                        queue.append(None)
                    ans.append(l)
                    l=[]
            return ans
        return (level(root,l,ans))
