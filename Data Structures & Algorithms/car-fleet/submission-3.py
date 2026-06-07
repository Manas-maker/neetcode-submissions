class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        road = sorted(zip(position, speed), reverse = True)
        times = []
        for i in road:
            time = (target-i[0])/i[1]
            if not times or times[-1]<time:
                times.append(time)
        return len(times)