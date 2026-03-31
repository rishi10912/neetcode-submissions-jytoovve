class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        mid = n//2
        # odd number
        if n %2 == 1:
            return self.arr[mid]
        else:
            n1 = self.arr[mid-1]
            n2 = self.arr[mid]
            return (n1+n2)/2

        
        