"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = sorted(intervals, key = lambda interval: interval.start)
        
        if not intervals:
                return 0
        
        rooms = []
        
        for time in meetings:
            if not rooms:
                heapq.heappush(rooms,time.end)
            elif rooms[0] <= time.start:
                heapq.heapreplace(rooms,time.end)
            else :
                heapq.heappush(rooms,time.end)

        
        return len(rooms)
