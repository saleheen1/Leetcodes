import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        def k_works(k):
            hours = 0
            for v in piles:
                # in python 2 or leetcode, use ceil like this
                hours += math.ceil(float(v)/k)
            return hours <=h
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left+right) // 2
            
            if k_works(mid):
                right = mid
            else:
                left = mid +1
        return left






s =Solution()
print(s.minEatingSpeed(piles=[30,11,23,4,20],h= 6))