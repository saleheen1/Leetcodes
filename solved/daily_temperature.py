class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = []
        result = [0] * len(temperatures)
        
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                stack_value,stack_index = stack.pop()
                result[stack_index] = i - stack_index
            
            stack.append((v,i))

        return result


            




solution = Solution()
print(solution.dailyTemperatures(temperatures=[30,40,50,60]))
            
         