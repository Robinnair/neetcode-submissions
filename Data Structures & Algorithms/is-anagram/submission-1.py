class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            if freq.get(ch,0)==0:
                return False
            else:
                freq[ch]=freq.get(ch,0)-1
        if all(value==0 for value in freq.values()):
            return True
        else:
            return False
        
        