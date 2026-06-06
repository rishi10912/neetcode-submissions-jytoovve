class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        result.append(intervals[0])

        for start,end in intervals[1:]:
            #end value of last interval in result
            lastEnd = result[-1][1]
            #overlapping case
            if start <= lastEnd:
                result[-1][1] = max(lastEnd,end)
            else:
                result.append([start,end])
        return result 
        