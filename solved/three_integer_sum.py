class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        for i,v in enumerate(nums):
            leftIndex = i+1
            rightIndex = len(nums) -1
            

            if i > 0 and v == nums[i-1]:
                continue
            
            while leftIndex < rightIndex:
                sum = v + nums[leftIndex] + nums[rightIndex]
                if sum > 0:
                    rightIndex -=1
                elif sum < 0:
                    leftIndex +=1
                else:
                    result.append([v,nums[leftIndex],nums[rightIndex]])
                    leftIndex +=1
                    rightIndex -=1
                    while nums[leftIndex] == nums[leftIndex -1] and leftIndex < rightIndex:
                        leftIndex +=1
        return result


            

        





s =Solution()
print(s.threeSum(nums=[-1,-1,0,1,1,1,2,2,6]))

