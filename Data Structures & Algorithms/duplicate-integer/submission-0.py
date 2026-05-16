class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited=set()
        for num in nums:
            visited.add(num)
        if len(visited)!=len(nums):
            return True
        else:
            return False