#Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: (x[0]))
        queue = []
        for interval in intervals:
            if queue and queue[0] <= interval[0]:
                heapq.heapreplace(queue, interval[1])
            else:
                heapq.heappush(queue, interval[1])
        return len(queue)