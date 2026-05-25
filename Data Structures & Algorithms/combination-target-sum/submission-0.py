class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output=[]
        def backtrack(start,remaining,path):
            if(remaining==0):
                output.append(path[:])
                return
            if(remaining<0):
                return
            for i in range(start,len(nums)):
                num=nums[i]
                path.append(num)
                backtrack(i,remaining-num,path)
                path.pop()

        backtrack(0,target,[])
        return output
