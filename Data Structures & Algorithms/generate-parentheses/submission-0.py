class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(cur,opencount,closedcount):
            if(len(cur)==2*n):
                ans.append(cur)
            if(opencount<n):
                backtrack(cur+"(",opencount+1,closedcount)
            if(closedcount<opencount):
                backtrack(cur+")",opencount,closedcount+1)
        backtrack("",0,0)
        return ans