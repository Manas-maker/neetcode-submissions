class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = [[] for _ in range(len(nums)+1)]
        counts = {}
        for i in nums:
            if i in counts: counts[i] += 1
            else: counts[i] = 1
        for i in counts:
            freq = counts[i]
            store[freq].append(i)
        out = []
        for i in range(len(store)-1, 0, -1):
            for j in store[i]:
                out.append(j)
                if len(out) == k:
                    return out
        