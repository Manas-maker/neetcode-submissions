class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            key = [0]*26
            for j in i:
                key[ord(j)-ord('a')] += 1
            key = tuple(key)
            if key in anagrams:
                anagrams[key].append(i)
            else: anagrams[key] = [i]

        return list(anagrams.values())