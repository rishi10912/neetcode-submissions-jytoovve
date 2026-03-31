class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0) +1
        
        arr = list(my_dict.items())
        arr.sort(key=lambda x:x[1], reverse =True)
        
        result = []

        for i in range(k):
            result.append(arr[i][0])
        return result
        