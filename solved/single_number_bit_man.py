class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = 0
        for x in nums:
            a ^= x
        return a


s = Solution()
print(s.singleNumber(nums=[1,2,3,2,1]))