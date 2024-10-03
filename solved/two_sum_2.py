class Solution(object):
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        leftIndex = 0
        rightIndex = len(numbers) - 1

        while leftIndex < rightIndex:

            sum = numbers[leftIndex] + numbers[rightIndex]
            if sum > target:
                rightIndex -=1
            elif sum < target:
                leftIndex +=1
            else:
                return [leftIndex +1,rightIndex +1]
            
            

            

        

s =Solution()
print(s.twoSum(numbers=[2,7,11,15],target=18))