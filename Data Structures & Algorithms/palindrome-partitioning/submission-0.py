class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def backtrack(start,path):
            if(start==len(s)):
                ans.append(path[:])
                return 
            for end in range(start+1,len(s)+1):
                sub=s[start:end]
                if sub==sub[::-1]:
                    path.append(sub)
                    backtrack(end,path)
                    path.pop()
        backtrack(0,[])
        return ans