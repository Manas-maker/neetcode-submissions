class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        nums.sort()
        i = 0
        print(nums)
        while i < len(nums)-2:
            if i>0 and nums[i]==nums[i-1]: 
                i += 1
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i]+nums[left]+nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    trips.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    left += 1
            i += 1
            
        return trips