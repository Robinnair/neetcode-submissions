class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        total_water=0
        i=0
        while(i<n-1):
            best=i+1
            for j in range(i+1,n):
                if(height[j]>height[i]):
                    best=j
                    break
                if height[j]>height[best]:
                    best=j
            water_level=min(height[i],height[best])
            for k in range(i+1,best):
                total_water+=max(0,water_level-height[k])
            i=best
        return total_water