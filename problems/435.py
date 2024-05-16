class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev_interval_index = overlapping_count = 0
        n = len(intervals)

        for i in range(1, n):
            if intervals[prev_interval_index][1] > intervals[i][0]:
                overlapping_count += 1
                continue
            
            prev_interval_index = i

        return overlapping_count