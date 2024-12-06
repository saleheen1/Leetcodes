class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # full equation: n/2 * (2a+(n-1)*d)
        # a = first value which is always zero in this case
        # d = difference between numbers which is always 1 in this case
        # so, the short equation in this case is
        # equation: (n/2) * (n-1)
        
        n = len(nums) + 1
        # doing len+1 because a number is missing from array as the problem says

        
        sum_total = (n/2) * (n-1)
        # converting float to int 
        sum_total = int(sum_total)
         
        # sum that should be minus sum that the array is giving to us
        # is the number that is missing
        return sum_total - sum(nums)
