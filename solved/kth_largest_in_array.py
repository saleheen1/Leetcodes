import heapq

class Solution:
    def findKthLargest(self, nums:list[int], k:int):
        values = nums
        for i in range(len(values)):
            values[i] = -values[i]
        
        heapq.heapify(values)

        for i in range(k-1):
            heapq.heappop(values)
        
        return -values[0]