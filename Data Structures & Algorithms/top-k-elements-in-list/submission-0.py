import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)

        heap=[]
        for num,count in freq.items():
            heapq.heappush(heap,(-count,num))
        
        ans=[]
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

        