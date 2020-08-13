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


#Task: Path Sum II from Leetcode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #same as the part 1, but with appending 
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        path = []
        if not root:
            return result
        
        self.appendPath(root, sum, 0, path, result)
        return result

    
    def appendPath(self, root, sum, pathsum, path, result):
        pathsum = pathsum + root.val
        path = path + root.val
        remainSum = sum - root.val
        if not root:
            return False
        else:
            path.append(root.val)
            if (root and not root.left and not root.right and root.val == sum):
                result.append(path)
                path = []
            else:
                self.appendPath(root.left, remainSum, pathsum, path, result) 
                self.appendPath(root.right, remainSum, pathsum, path, result)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __jnit__(self):
        self.acc_map = {0: 1}

    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.pathSumRecursive(root, 0, sum)

    def pathSumRecursive(self, root, acc, sum):
        if not root:
            return 0 #false

        current_acc = acc + root.val
        self.acc_map.setdefault(current_acc, 0)
        self.acc_map[current_acc] += 1
        left_sum = self.pathSumRecursive(root.left, current_acc, sum)
        right_sum = self.pathSumRecursive(root.right, current_acc, sum)
        self.acc_map[current_acc] -= 1

        return self.acc_map.get(current_acc - sum, 0) + left_sum + right_sum

        

