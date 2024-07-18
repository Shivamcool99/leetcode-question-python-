# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
      
        self.result = 0
        
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [(node, 0)]
            
            left_paths = dfs(node.left)
            right_paths = dfs(node.right)
            
            paths = []
            for (left_node, left_dist) in left_paths:
                if left_node.left is None and left_node.right is None:
                    paths.append((left_node, left_dist + 1))
                else:
                    paths.extend([(n, d + 1) for n, d in left_paths])
            
            for (right_node, right_dist) in right_paths:
                if right_node.left is None and right_node.right is None:
                    paths.append((right_node, right_dist + 1))
                else:
                    paths.extend([(n, d + 1) for n, d in right_paths])
                    
            for (left_node, left_dist) in left_paths:
                for (right_node, right_dist) in right_paths:
                    total_dist = left_dist + right_dist + 2
                    if total_dist <= distance:
                        self.result += 1
            
            return paths
        
        dfs(root)
        return self.result
        