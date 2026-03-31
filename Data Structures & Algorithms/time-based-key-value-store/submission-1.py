class TimeMap:

    def __init__(self):
        self.my_dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        seen = 0 
        result =""
        for time,value in self.my_dict[key]:
            if time <= timestamp and time > seen:
                seen = time
                result = value
        return result

        
