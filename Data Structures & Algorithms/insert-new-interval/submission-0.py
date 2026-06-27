class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        newStart,newEnd= newInterval
        for start,end in intervals:
            if end<newStart:
                ans.append([start,end])
            elif newEnd<start:
                ans.append([newStart,newEnd])
                newStart,newEnd=start,end
            else:
                newStart=min(newStart,start)
                newEnd=max(newEnd,end)
        ans.append([newStart,newEnd])
        return ans


        
