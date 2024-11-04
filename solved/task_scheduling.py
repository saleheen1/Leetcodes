from collections import deque
from typing import Counter
import heapq

class Solution:
    def leastInterval(self,tasks: list[str], n: int) -> int:

        dataDict = Counter(tasks)

        maxHeap = [-v for v in dataDict.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time +=1
            if maxHeap:
                topHeapValue = 1 + heapq.heappop(maxHeap)
                if topHeapValue:
                    q.append([topHeapValue, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time


