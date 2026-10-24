# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: TreeNode, depth: int, res: List[List[int]]):
        if len(res) == depth:
            res.append([root.val])
        else:
            res[depth].append(root.val)
        if root.left:
            self.traverse(root.left, depth + 1, res)
        if root.right:
            self.traverse(root.right, depth + 1, res)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.traverse(root, 0, res)
        return res
        