class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxAr = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1]>heights[i]: 
                last = stack.pop()
                ar = (i-last[0])*last[1]
                maxAr = max(maxAr, ar)
                index = last[0]
            stack.append([index, heights[i]])
        while stack:
            last = stack.pop()
            ar = (len(heights)-last[0])*last[1]
            maxAr = max(maxAr, ar)
        return maxAr