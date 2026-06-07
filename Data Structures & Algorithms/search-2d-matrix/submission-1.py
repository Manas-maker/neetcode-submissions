class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b, l, r = 0, len(matrix)-1, 0, len(matrix[0])-1
        while t<b:
            vm = (t+b)//2
            if matrix[vm][-1]<target:
                t = vm + 1
            else:
                b = vm
        while l<r:
            hm = (l+r)//2
            if matrix[t][hm]<target:
                l = hm + 1
            else:
                r = hm 
        print(matrix[t][l], t, l)
        return True if t<len(matrix) and l<len(matrix[0]) and matrix[t][l]== target else False