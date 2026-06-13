class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*(-1) for i in stones]
        heapq.heapify(stones)
        while (len(stones)>1):
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            if x == y: continue
            else: heapq.heappush(stones, y-x)
        return 0 if not stones else -stones[0]
            

