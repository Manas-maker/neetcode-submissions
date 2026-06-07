class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        test = list(hashmap.items())
        test.sort(key = lambda x:x[1], reverse = True)
        out = [test[i][0] for i in range(k)]
        return out