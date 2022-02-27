# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = [{'node' : root, 'depth' : 1}]
        max_depth = 0
        while len(queue) > 0:
            node_dict = queue.pop()
            node = node_dict['node']
            if node is None:
                continue
            depth = node_dict['depth']
            max_depth = max(depth, max_depth)
            queue += [{'node' : node.left, 'depth' : depth+1}, {'node' : node.right, 'depth' : depth+1}]
            
        return max_depth
