class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0) +1
        
        buckets = [[] for i in range(len(nums)+1)]
        for num,frequency in my_dict.items():
            buckets[frequency].append(num) # Bucket[1] : 1
        
        result = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        