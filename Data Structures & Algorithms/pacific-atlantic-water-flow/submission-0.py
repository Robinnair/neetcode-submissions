class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=set()
        atlantic=set()
        row=len(heights)
        col=len(heights[0])
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r,c,visited):
            for dr,dc in direction:
                nr=dr+r
                nc=dc+c
                if(nr<0 or nc<0 or nr>=row or nc>=col or (nr,nc) in visited or heights[nr][nc]<heights[r][c]):
                    continue
                visited.add((nr,nc))
                dfs(nr,nc,visited)
        for r in range(row):
            pacific.add((r,0))
            dfs(r,0,pacific)
        for c in range(col):
            pacific.add((0,c))
            dfs(0,c,pacific)
        for r in range(row):
            atlantic.add((r,col-1))
            dfs(r,col-1,atlantic)
        for c in range(col):
            atlantic.add((row-1,c))
            dfs(row-1,c,atlantic)
        output=[]
        for r in range(row):
            for c in range(col):
                if((r,c) in pacific and (r,c) in atlantic):
                    output.append((r,c))
        return output