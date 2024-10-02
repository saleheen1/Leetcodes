class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        rightM = 1

        for i in range(len(nums)):
            if i==0:
                result.append(nums[i])
                continue
            leftM = nums[i] * result[i-1]
            result.append(leftM)
        
        for i in reversed(range(len(nums))):
            if i == len(nums) -1:
                result[i] = result[i-1]
                rightM = nums[i]
                continue

            if i == 0:
                result[i] = rightM
                return result
            result[i] = result[i-1] * rightM
            rightM = nums[i] * rightM
            







s =Solution()
print(s.productExceptSelf(nums=[4,3,2,1,2]))