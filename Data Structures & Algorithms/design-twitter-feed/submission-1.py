class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = []
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([tweetId, userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        i, out, j = 0, [], len(self.tweets)-1
        while j>-1 and i<10 and self.tweets:
            if ((self.tweets[j][1] == userId) or (userId in self.users and self.tweets[j][1] in self.users[userId])):
                out.append(self.tweets[j][0])
                i+=1
            j-=1

        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].add(followeeId)
        else: self.users[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
