class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1={}
        for ch in s1:
            freq1[ch]=freq1.get(ch,0)+1
        size=len(s1)
        for i in range(0,len(s2)):
            freq2={}
            if(i+size>len(s2)):
                break
            for ch in s2[i:i+size]:
                freq2[ch]=freq2.get(ch,0)+1
            if all(freq1.get(ch,0)==freq2.get(ch,0) for ch in s1):
                return True
        return False