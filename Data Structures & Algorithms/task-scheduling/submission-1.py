class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        out = 0
        tasksLeft = len(tasks)
        freqs = [[0, chr(i+ord('A'))] for i in range(26)]
        for i in tasks:
            freqs[ord(i)-ord('A')][0] -= 1
        heapq.heapify(freqs)
        lastUsed = {}
        i = 0
        while tasksLeft>0:
            freq, char = heapq.heappop(freqs)
            tmp = []
            while freq != 0 and char in lastUsed and i-lastUsed[char]<=n:
                tmp.append([freq, char])
                freq, char = heapq.heappop(freqs)
            if freq!=0:
                lastUsed[char] = i
                freq += 1
                tasksLeft -= 1
            tmp.append([freq, char])
            for c in tmp:
                heapq.heappush(freqs, c)
            i += 1
            out += 1
        return out
            