from collections import defaultdict
class Solution:
    def longestSeq (self,nums:list[int])->int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        longest = 1

        for v in num_set:
            long = 1
            if v -1 in num_set:
                continue
            while (v + long) in num_set:
                long +=1
                longest = max(longest,long)
        return longest







s = Solution()
print(s.productExceptSelf(nums=[1,2,4,6]))