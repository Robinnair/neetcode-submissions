class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in nums:
            if(freq.get(num,0)>1):
                return num