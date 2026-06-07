class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dat = {}
        for i in nums:
            if i in dat:
                return True
            else:
                dat[i] = [1]
        return False