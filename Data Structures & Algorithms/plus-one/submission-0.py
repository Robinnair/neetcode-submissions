class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int(''.join(map(str,digits)))
        num+=1
        digi=[]
        while(num!=0):
            digi.append(num%10)
            num=num//10
        digi.reverse()
        return digi