class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        l, r = 0, len(nums)-1
        while l<=r:
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i]<=pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p>k: l, r = l, p-1
            elif p<k: l, r = p+1, r
            else: return nums[p]
            