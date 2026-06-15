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
        totalTweets = []
        if userId in self.tweets:
            totalTweets += [tweet for tweet in self.tweets[userId]]
        if userId in self.users:
            totalTweets += [tweet  for i in self.users[userId] for tweet in self.tweets.get(i, [])]
        print(totalTweets)
        heapq.heapify(totalTweets)
        print(totalTweets)
        out = []
        while totalTweets and len(out)<10:
            out.append(heapq.heappop(totalTweets)[1])
        return out
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.users:
                self.users[followerId].add(followeeId)
            else: self.users[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)
