class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        res = []
        curr = collections.deque()
        for i in range(0, len(nums)):
            while len(curr)>0 and nums[i]>=curr[-1][0]:
                curr.pop()
            curr.append((nums[i], i))
            if i>=(k-1):
                while curr[0][1]<l:
                    curr.popleft()
                res.append(curr[0][0])
                l, r = l+1, r+1
        return res