class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        ithToLeft = []
        ithToRight = []
        stack = []
        maxArea = 0

        # Getting how far we can go from i'th to left 
        for i in range(len(heights)):
            if i==0:
                stack.append(i)
                ithToLeft.append(i)
                continue

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if len(stack) == 0 :
                ithToLeft.append(0)
            else:
                ithToLeft.append(stack[-1] + 1)

            stack.append(i)
        
        # Getting how far we can go from i'th to right
        stack.clear()

        for i in reversed(range(len(heights))):
            
            if i== (len(heights) -1):
                stack.append(i)
                ithToRight.append(i)
                continue
            
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if len(stack) == 0 :
                ithToRight.append(len(heights) -1)
            else:
                ithToRight.append(stack[-1] - 1)

            stack.append(i)

        ithToRight.reverse()

        # Get max area
        for i in range(len(heights)):
            area = ((ithToRight[i] - ithToLeft[i]) + 1) * heights[i]
            maxArea = max(maxArea,area)
        
        return maxArea



s =Solution()
print(s.largestRectangleArea(heights=[1,3,7]))