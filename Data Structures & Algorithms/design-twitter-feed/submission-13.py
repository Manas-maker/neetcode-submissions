class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.count = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append([self.count, tweetId])
        else:
            self.tweets[userId] = [[self.count, tweetId]]
        self.count -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        if userId in self.users:
            self.users[userId].add(userId)
        else: self.users[userId] = {userId}
        for followeeId in self.users[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res)<10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.users:
                self.users[followerId].add(followeeId)
            else: self.users[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)
