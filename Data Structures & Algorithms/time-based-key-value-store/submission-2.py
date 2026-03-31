class TimeMap:

    def __init__(self):
        self.my_dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        arr = self.my_dict[key]
        left,right = 0,len(arr)-1
        result = ""

        while left <= right:
            mid = (left+right)//2
            # potentail result but still move right to find latest
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                left = mid+1
            else:
                right = mid-1
        return result

        
