class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        dataSet = set()
        for value in nums:
            if(value in dataSet):
                return True
            dataSet.add(value)
            
        return False
            


solution = Solution()
print(solution.hasDuplicate( nums=[1,2,3,5]))
            
         