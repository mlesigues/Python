#Task: Vertical Order Traversal of a Binary Tree from Leetcode
#src:https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/
#src:https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/253965/Python-8-lines-array-and-hashmap-solutions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        #the horizontal distance of root is set to 0 => root: (x,y) = (0,0)
        
        #will be used for the vertical nodes, min and max vertical indices
        self.dic = collections.defaultdict(list)
        
        """"
        self.minimumLevel, self.maximumLevel = float("inf"), -float("inf")
        
        #dfs function: takes in root, horizontal coordinate, vertical coordinate
        def dfs(root, hor, ver):
            self.maximumLevel = min(hor, self.minimumLevel)
            self.minimumLevel = max(hor, self.maximumLevel)
            dic[hor].append((ver, root.val))
            if root.left:
                dfs(root.left, hor-1, ver+1)
            if root.right:
                dfs(root.right, hor+1, ver+1)
                
            dfs(root, 0,0)
            result = []
            for i in range(self.minimumLevel, self.maximumLevel + 1):
                result += [[i for i,j in sorted(dic[i])]]
            return result
        """
        
        def dfs(node, hor, ver):
            if node:
                self.dic[hor].append((ver, node.val))
                dfs(node.left, hor - 1, ver + 1)
                dfs(node.right, hor + 1, ver + 1)
        
        dfs(root, 0, 0)
        
        return [list(map(lambda hor: hor[1], sorted(arr))) for x, arr in sorted(self.dic.items())]