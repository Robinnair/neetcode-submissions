# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root==None):
            return []
        q=deque()
        q.append(root)
        output=[]
        while(q):
            level=[]
            size=len(q)
            for _ in range(size):
                cur=q.popleft()
                level.append(cur.val)
                if(cur.left!=None):
                    q.append(cur.left)
                if(cur.right!=None):
                    q.append(cur.right)
            output.append(level[-1])
        return output
            