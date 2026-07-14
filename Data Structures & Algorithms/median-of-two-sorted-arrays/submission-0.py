class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = []
        i1, i2 = 0, 0
        m, n = len(nums1), len(nums2)
        while i1<m and i2<n:
            if nums1[i1]<nums2[i2]:
                new.append(nums1[i1])
                i1 += 1
            else:
                new.append(nums2[i2])
                i2 += 1
        while i1<m:
            new.append(nums1[i1])
            i1 += 1
        while i2<n:
            new.append(nums2[i2])
            i2 += 1
        print(new)
        return new[(m+n)//2] if (m+n)%2==1 else (new[(m+n)//2]+new[(m+n)//2-1])/2