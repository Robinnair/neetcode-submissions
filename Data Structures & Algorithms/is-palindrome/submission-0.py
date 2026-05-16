class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=""
        for ch in s:
            if(ch.isalnum()):
                strs+=ch.lower()
        start=0
        end=len(strs)-1
        while(start<end):
            if(strs[start]!=strs[end]):
                return False
            start+=1
            end-=1
        return True
        