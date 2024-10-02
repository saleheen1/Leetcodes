class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            length = 1
            if nums[i]-1 in numSet:
                continue
            
            while (nums[i] + length) in numSet:
                length +=1
                
            longest = max(length, longest)

        return longest



s =Solution()
print(s.longestConsecutive(nums=[2,20,4,10,3,]))