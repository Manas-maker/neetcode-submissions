class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newHeap = []
        for i in nums:
            heapq.heappush(newHeap, i)
            if len(newHeap)>k: heapq.heappop(newHeap)
        return newHeap[0]