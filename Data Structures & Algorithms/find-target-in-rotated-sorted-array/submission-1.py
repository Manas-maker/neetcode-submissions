class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m
        #search on right
        sl, sr = l, len(nums) - 1
        while sl<=sr:
            m = (sl+sr)//2
            if nums[m] == target:
                return m
            elif target>nums[m]:
                sl = m+1
            else:
                sr = m - 1
        #search on left
        sl, sr = 0, l-1
        while sl <= sr:
            m = (sl+sr)//2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                sl = m+1
            else:
                sr = m - 1
        return -1
