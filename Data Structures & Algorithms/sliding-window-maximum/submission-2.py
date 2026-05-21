class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi=-float("inf")
        output=[]
        for i in range(k):
            maxi=max(nums[i],maxi)
        output.append(maxi)
        for i in range(1,len(nums)):
            if(i+k-1==len(nums)):
                break
            if(maxi in nums[i:i+k]):
                maxi=max(maxi,nums[i+k-1])
            else:
                maxi=max(nums[i:i+k])
            output.append(maxi)
        return output
        
