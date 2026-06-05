class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            #Case1: Non-overlapping, new interval ends before the current
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            #Case 2: Non overlapping, new interval in between existing intervals
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            #overlapping
            else:
                #merge
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        result.append(newInterval)
        return result
        