from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time,tweetId))
        self.time +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []
        #Edge case, user follows self
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            # if tweets exist
            if self.tweetMap[followee]:
                index = len(self.tweetMap[followee])-1
                time,tweet = self.tweetMap[followee][index]
                heapq.heappush(heap,(-time,tweet,followee,index-1))
        while heap and len(result) <10:
            negTime,tweet, followee,index = heapq.heappop(heap)
            result.append(tweet)
            if index >=0:
                time, tweet = self.tweetMap[followee][index]
                heapq.heappush(heap,(-time, tweet, followee, index - 1))
        return result


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard isntaed of remove so that no error if false followeeId
        self.followMap[followerId].discard(followeeId) 
        
