class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        dataDict = {}
        for value in nums:
            if(dataDict.get(value,0) ==1):
                return True
            dataDict[value] = dataDict.get(value, 0) +1;
            
        return False
            


solution = Solution()
print(solution.hasDuplicate( nums=[1,2,3,1]))
            
         