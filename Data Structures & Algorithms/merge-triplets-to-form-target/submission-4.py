class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def merge(trip1, trip2):
            return [max(trip1[0], trip2[0]), max(trip1[1], trip2[1]), max(trip1[2], trip2[2])]
        def search(root_idx, cur):
            if cur==target: return True
            candidate_idx = root_idx + 1
            while cur!=target and candidate_idx<len(triplets):
                for i in range(3):
                    while triplets[candidate_idx][i]>target[i]:
                        candidate_idx+=1
                        if candidate_idx>=len(triplets): return False
                for i in range(3):
                    if triplets[candidate_idx][i]==target[i]:
                        merged = merge(cur, triplets[candidate_idx])
                        if merged==target:
                            return True
                        else:
                            return search(candidate_idx, merged)
                candidate_idx += 1
            return False
                        

        for root_idx in range(len(triplets)):
            for i in range(3):
                if triplets[root_idx][i]>target[i]:
                    break
            else:
                cur = triplets[root_idx].copy()
                check = search(root_idx, cur)
                return check
        return False