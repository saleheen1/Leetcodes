import heapq

class Solution:
    def lastStoneWeight(self, stones:list[int]):
        
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            if largest != second_largest:
                heapq.heappush(stones, largest-second_largest)
        
        if len(stones) == 1:
            return  -stones[0]
        else:
            return 0