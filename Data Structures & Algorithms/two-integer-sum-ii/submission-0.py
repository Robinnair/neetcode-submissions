class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        for i in range(len(numbers)):
            for j in range(i,len(numbers)):
                if(numbers[i]+numbers[j]==target):
                    output.append(i+1)
                    output.append(j+1)
                    return output
        