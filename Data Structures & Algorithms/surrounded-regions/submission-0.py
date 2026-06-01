class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q=deque()
        visited=set()
        rows=len(board)
        cols=len(board[0])
        for r in range(rows):
            if(board[r][0]=="O"):
                visited.add((r,0))
                q.append((r,0))
            if(board[r][cols-1]=="O"):
                visited.add((r,cols-1))
                q.append((r,cols-1))
        for c in range(cols):
            if(board[0][c]=="O"):
                visited.add((0,c))
                q.append((0,c))
            if(board[rows-1][c]=="O"):
                visited.add((rows-1,c))
                q.append((rows-1,c))
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        while(q):
            r,c=q.popleft()
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if(nr<0 or nc<0 or nr>=rows or nc>=cols or board[nr][nc]!="O" or (nr,nc) in visited):
                    continue
                visited.add((nr,nc))
                q.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if((r,c) not in visited and board[r][c]=="O"):
                    board[r][c]="X"
