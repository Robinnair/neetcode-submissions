class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])

        q=deque()
        fresh=0

        for r in range(row):
            for c in range(col):
                if(grid[r][c]==2):
                    q.append((r,c))
                elif(grid[r][c]==1):
                    fresh+=1
        minutes=0
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in direction:
                    nr=dr+r
                    nc=dc+c
                    if(nr<0 or nc<0 or nr>=row or nc>=col or grid[nr][nc]!=1):
                        continue
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc))
            minutes+=1
        return minutes if fresh==0 else -1