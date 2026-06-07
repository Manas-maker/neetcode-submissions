class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in numset:
            if i-1 not in numset:
                run = 1
                while i + run in numset:
                    run += 1
                longest = max(longest, run)
        return longest

