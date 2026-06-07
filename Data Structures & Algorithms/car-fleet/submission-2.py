class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        road = [[]]*len(position)
        for i in range(len(position)):
            road[i] = [position[i], speed[i]]
        road.sort(key = lambda x: (x[0]), reverse = True)
        i = 0
        print(road)
        while i<(len(road)-1):
            if (target-road[i][0])/road[i][1] >= (target-road[i+1][0])/road[i+1][1]:
                road.pop(i+1)
            else:
                i += 1
        print(road)
        return len(road)