class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i!=j:
                    if(nums[i]+nums[j]==target):
                        ans=[i,j]
                        return ans
        return [None,None]
                    
        