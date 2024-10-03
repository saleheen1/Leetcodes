class Solution:
    def trap(self, height: list[int]) -> int:
        waterContained = 0
        leftMaxBarArray =  []
        rightMaxBarArray =  []
        leftMaxBar = 0
        rightMaxBar = 0
        
        # save left max bar for each bar
        # in the same index of height[] we are saving the max of left in another array
        for i in range(len(height)):
            if i==0:
                leftMaxBar = 0
            else:
                leftMaxBar = max (leftMaxBar,height[i - 1])
            leftMaxBarArray.append(leftMaxBar)

        # save right max bar for each bar
        for i in reversed(range(len(height))):
            
            if i== len(height) -1:
                rightMaxBar = 0
                rightMaxBarArray.append(rightMaxBar)
                continue
            # elif i == 0:
            #     print('here in zero now')
            #     rightMaxBarArray[:0] = [0]
            #     continue
            else:
                
                rightMaxBar = max (rightMaxBar,height[i+1])
                
            rightMaxBarArray.append(rightMaxBar)
        rightMaxBarArray.reverse()

        # find water that each bar has on it's top
        for i in range(len(height)):
            waterLevel = 0
            # print('for value ', height[i] , 'max in left ', leftMaxBarArray[i], ' max on right ', rightMaxBarArray[i])

            if leftMaxBarArray[i] < height[i] or rightMaxBarArray[i] < height[i]:
                continue

            waterLevel = min(leftMaxBarArray[i], rightMaxBarArray[i])
            print('left max ',leftMaxBarArray[i], ' right max ', rightMaxBarArray[i])
            print('water level for ',height[i], 'is ',waterLevel)

            waterInCurrentBar = waterLevel - height[i]
            waterContained += waterInCurrentBar
        
        return waterContained



        


s =Solution()
print(s.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))