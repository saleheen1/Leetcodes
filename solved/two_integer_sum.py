class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashData = {}
        subtRes = 0

        for i in range(len(nums)):
            hashData[nums[i]] = i

        for i in range(len(nums)):
            subtRes =  target - nums[i]
            # print('current index ',i,'current array value ', nums[i])
            if subtRes in hashData and i != hashData[subtRes]:
                # print("index is ",hashData[subtRes], "key is ",subtRes)
                return [i, hashData[subtRes]]

        

solution = Solution()
res =solution.twoSum(nums = [3,2,4], target=6)
print(res)