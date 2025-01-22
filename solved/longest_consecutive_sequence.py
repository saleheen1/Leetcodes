class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        longest = 1

        for v in num_set:
            long = 1
            if (v -1) not in num_set:
                while (v + long) in num_set:
                    long +=1
                    longest = max(longest,long)
        return longest



s =Solution()
print(s.longestConsecutive(nums=[2,20,4,10,3,]))