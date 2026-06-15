class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        newTasks = [[0, chr(i+ord('A'))] for i in range(26)]
        for i in range(len(tasks)):
            newTasks[ord(tasks[i])-ord('A')][0] -= 1
        heapq.heapify(newTasks)
        cooldown = []
        tasksLeft = len(tasks)
        i = 0
        while tasksLeft != 0:
            if not cooldown and newTasks[0][0] == 0:
                break
            #cooldown[i][char, remaining occurences, timeWhenFree]
            j = 0
            while j<len(cooldown):
                if cooldown[j][2] == i:
                    char, freq, cd = cooldown.pop(j)
                    heapq.heappush(newTasks, [freq, char])
                j += 1
            if newTasks and newTasks[0][0] != 0:
                remainingFreq, char = heapq.heappop(newTasks)
                if remainingFreq<-1:
                    cooldown.append([char, remainingFreq+1, i+n+1])
                tasksLeft -= 1
            i+=1

        return i