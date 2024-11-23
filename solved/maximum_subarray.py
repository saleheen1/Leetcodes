class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        max_sum = float('-inf')
        curr_sum = 0

        for v in nums:
            curr_sum = v
            max_sum = max(max_sum,curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum
            
