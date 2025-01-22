class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        result = []
        product = 1

        for i in range(len(nums)):
            if i==0:
                result.append(nums[i])
                continue
            leftM = nums[i] * result[i-1]
            result.append(leftM)

        
        for i in reversed(range(len(nums))):
            if i == len(nums) -1:
                result[i] = result[i-1]
                product = nums[i]
                continue

            if i == 0:
                result[i] = product
                return result
            
            result[i] = result[i-1] * product
            product = nums[i] * product
            


s =Solution()
print(s.productExceptSelf(nums=[4,3,2,1,2]))