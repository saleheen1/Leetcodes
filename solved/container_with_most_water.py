class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        maxArea = 0
        leftIndex = 0;
        rightIndex = len(height) -1

        while leftIndex < rightIndex:
            width = abs(leftIndex - rightIndex)
            smallBar = 0
            smallBar = min(height[leftIndex], height[rightIndex])
            area = width * smallBar
            maxArea = max(maxArea,area)

            if height[leftIndex] > height[rightIndex]:
                rightIndex -=1
            else:
                leftIndex +=1
        
        return maxArea






s = Solution()
print(s.maxArea( height=[1,7,2,5,4,7,3,6]))
            
         