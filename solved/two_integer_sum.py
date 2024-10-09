class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashData = {}
        subtRes = 0

        for i in range(len(nums)):
            hashData[nums[i]] = i

        for i in range(len(nums)):
            subtRes =  target - nums[i]
            if subtRes in hashData and i != hashData[subtRes]:
                return [i, hashData[subtRes]]

        

solution = Solution()
res =solution.twoSum(nums = [3,2,4], target=6)
print(res)