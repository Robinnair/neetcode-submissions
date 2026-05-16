class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        for num in nums:
            prod=prod*num
        output=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                output.append(prod//nums[i])
            else:
                pro=1
                for j in range(len(nums)):
                    if j!=i:
                        pro=pro*nums[j]
                output.append(pro)

        return output
        