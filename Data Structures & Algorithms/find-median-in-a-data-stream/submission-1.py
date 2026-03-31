import heapq

class MedianFinder:

    def __init__(self):
        # max heap with smaller vals
        self.small = []
        # min heap with larger vals
        self.large = []
        

    def addNum(self, num: int) -> None:
        # num greater than the smallest element in large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-1*num)
        # balance
        if len(self.small) > len(self.large)+1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            n1 = -1 * self.small[0]
            n2 = self.large[0]
            return (n1+n2)/2
        
        