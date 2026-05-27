class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def backtrack(path):
            if(len(path)==len(nums)):
                output.append(path[:])
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
        backtrack([])
        return output