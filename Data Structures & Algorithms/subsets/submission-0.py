class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power = [[]]
        for i in nums:
            extras = []
            for j in power:
                extras.append(j.copy())
                j.append(i)
            power += extras
        return(power)