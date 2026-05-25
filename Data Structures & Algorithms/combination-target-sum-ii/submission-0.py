class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output=[]
        def backtrack(start,remaining,path):
            if(remaining==0):
                output.append(path[:])
                return
            if(remaining<0):
                return
            for i in range(start,len(candidates)):
                if(i>start and candidates[i]==candidates[i-1]):
                    continue
                num=candidates[i]
                path.append(num)
                backtrack(i+1,remaining-num,path)
                path.pop()
        backtrack(0,target,[])
        return output