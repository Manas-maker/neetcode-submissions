class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(lambda: [1, 1])
        for i in range(1, len(nums)):
            hashmap[i][0] = hashmap[i-1][0]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            hashmap[i][1] = hashmap[i+1][1]*nums[i+1]
        out = [hashmap[i][0]*hashmap[i][1] for i in range(len(nums))]
        print(out)
        return out