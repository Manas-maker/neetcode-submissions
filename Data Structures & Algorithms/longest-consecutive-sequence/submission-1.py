class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = defaultdict(set)
        longest = 0
        for i in nums:
            if i-1 not in nums:
                starts[i].add(i)
                longest = 1
        for i in starts:
            run = 1
            while i + run in nums:
                run += 1
                if run > longest:
                    longest = run
        return longest

