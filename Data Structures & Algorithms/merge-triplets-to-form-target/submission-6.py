class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = [False, False, False]
        for triplet in triplets:
            for i in range(3):
                if triplet[i]>target[i]:
                    break
            else:
                for i in range(3):
                    if triplet[i]==target[i]:
                        check[i]=True
        return all(check)