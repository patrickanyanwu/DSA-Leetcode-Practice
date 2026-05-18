"""
Design Twitter using a hashmap of tweet lists per user and a hashmap of followee sets per user.
Tweets are stored with a global decrementing counter so that more recent tweets have smaller (more negative) values, allowing a min heap to naturally surface the most recent tweets first.
For getNewsFeed, seed the heap with the most recent tweet from each followee (including the user themselves).
Then greedily pop the most recent tweet, append it to results, and push the next tweet from that same followee if one exists — this merges k sorted lists in O(k log k) per step.
Stop once 10 tweets are collected or the heap is empty.
postTweet: O(1), follow/unfollow: O(1), getNewsFeed: O(k log k) where k is the number of followees, O(n) space for all tweets and follow relationships.
"""

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)