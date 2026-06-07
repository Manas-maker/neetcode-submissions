class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxWater = None
        while l<r:
            if maxWater is None:
                maxWater = min(heights[l], heights[r])*(r)
            elif heights[l]<heights[r]:
                l+=1
                maxWater = max(maxWater, min(heights[l], heights[r])*(r-l))
            else:
                r-=1
                maxWater = max(maxWater, min(heights[l], heights[r])*(r-l))
        return maxWater