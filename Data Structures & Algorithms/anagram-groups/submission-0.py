class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in hashmap:
                hashmap[s].append(i)
            else:
                hashmap[s] = [i]
        return list(hashmap.values())