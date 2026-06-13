class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in points:
            distance = (i[0]**2+i[1]**2)
            heapq.heappush(distances, (-distance, i))
            if len(distances)>k:
                heapq.heappop(distances)
        out = [i[1] for i in distances]
        return out