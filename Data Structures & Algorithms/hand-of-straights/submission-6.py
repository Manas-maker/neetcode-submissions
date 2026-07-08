class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0: return False
        hand.sort()
        counts = {}
        i=0
        maxCard = 0
        for k in hand:
            if k not in counts:
                counts[k]=1
                maxCard = max(maxCard, k)
            else: counts[k] += 1
        for i in counts:
            if counts[i]>0:
                freq = counts[i]
                for j in range(groupSize):
                    if (i+j) not in counts: return False
                    counts[i+j]-=freq
                    if counts[i+j]<0: return False
        return all(counts[i]==0 for i in counts)