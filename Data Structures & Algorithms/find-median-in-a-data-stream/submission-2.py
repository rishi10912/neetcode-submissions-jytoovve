import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] #max heap (simulated)
        self.large = [] #min heap
        

    def addNum(self, num: int) -> None:
        # which heap to push?
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)
        #almost same number of elements 
        if len(self.small) > len(self.large)+1:
            val = -1* heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        elif len(self.small) +1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-val)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            n1 = -1*self.small[0]
            n2 = self.large[0]
            return (n1+n2)/2
        
        