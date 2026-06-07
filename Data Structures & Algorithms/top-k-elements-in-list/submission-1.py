class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        buck = [[] for _ in range(len(nums)+1)]
        for num, freq in hashmap.items():
            buck[freq].append(num)
        out = []
        for i in range(len(buck)-1, -1, -1):
            for j in buck[i]:
                out.append(j)
                if len(out)==k:
                    return out