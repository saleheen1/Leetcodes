class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        curr_max = 1
        curr_min = 1

        for v in nums:
            if v == 0:
                curr_max = 1
                curr_min = 1
                continue

            temp = curr_max * v
            curr_max = max(temp, curr_min * v, v)
            curr_min = min(temp, curr_min * v, v)
            res = max(res, curr_max, curr_min)
        
        return res