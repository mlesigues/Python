#Task: Path Sum from Leetcode
#Definition for a binary tree node.
# Definition for a binary tree node.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""  

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #from gfg: subract each node from the sum when going down, and 
        #check if the sum if 0 when no more subtrees left
        
        #if run out of tree, return sum is 0/true
        if not root:
            return False
        else:
            
            #check both subtrees
            remainSum = sum - root.val
            
            #check the sum of both subtrees and if it's 0, return true
            if(root and not root.left and not root.right and root.val == sum):
                return True
            """"
            #if left subtree is none, call hasPathSum and left subtree
            if (root.left is not None):
                self.hasPathSum(root.left, remainSum)
            
            if (root.right is not None):
                self.hasPathSum(root.right, remainSum)
            """
            
            #return remainSum
            return self.hasPathSum(root.left, remainSum) or self.hasPathSum(root.right, remainSum)
            