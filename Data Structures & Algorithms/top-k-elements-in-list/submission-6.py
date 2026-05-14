from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make freq map
        count = defaultdict(int)
        result = []
        for n in nums:
            count[n] +=1
        # create buckets
        buckets =[[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        # Get top K elements
        result = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result


