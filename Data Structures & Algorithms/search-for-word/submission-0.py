class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(i,j,k):
            if(len(word)==k):
                return True
            if(i<0 or j<0 or i>=len(board) or j>=len(board[0])):
                return False
            temp=board[i][j]
            if(word[k]!=board[i][j]):
                return False
            board[i][j]="#"
            found=backtrack(i+1,j,k+1) or backtrack(i-1,j,k+1) or backtrack(i,j+1,k+1) or backtrack(i,j-1,k+1)
            board[i][j]=temp
            if(found):
                return found


        for i in range(len(board)):
            for j in range(len(board[0])):
                if(backtrack(i,j,0)):
                    return True
        return False