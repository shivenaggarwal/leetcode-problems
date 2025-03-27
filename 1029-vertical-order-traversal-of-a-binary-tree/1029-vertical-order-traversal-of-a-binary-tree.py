# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output_items = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        res = [] 

        min_col = float('inf')
        max_col = float('-inf')

        while queue:
            node, row, col = queue.popleft()

            if col < min_col:
                min_col = col
        
            if col > max_col:
                max_col = col

            output_items[col].append((node.val, row))

            if node.left:
                queue.append((node.left, row+1, col-1))

            if node.right:
                queue.append((node.right, row+1, col+1))

        for column in range(min_col, max_col + 1):
            items = output_items[column]
            items.sort(key=lambda x: (x[1], x[0]))
            items = [val for val, _ in items]
            res.append(items)

        return res

