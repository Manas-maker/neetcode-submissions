class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        res = []
        curr = []
        for i in range(k):
            if curr == []:
                curr = [nums[i], i]
            elif nums[i]>curr[0]:
                curr = [nums[i], i]
        res.append(curr[0])
        for i in range(k, len(nums)):
            l, r = l+1, r+1
            if nums[i]>curr[0]:
                curr = [nums[i], i]
            elif curr[1]<l:
                curr = []
                for j in range(l, r+1):
                    if curr == []:
                        curr = [nums[j], j]
                    elif nums[j]>curr[0]:
                        curr = [nums[j], j]
            res.append(curr[0])
        return res