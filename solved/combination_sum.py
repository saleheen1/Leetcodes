
class Solution:
    def combinationSum(self,candidates:list[int],target:int):
        sol,res = [],[]
        nums = candidates

        def backtrack(i,curr_sum):
            if curr_sum == target:
                res.append(sol.copy())
                return
            if curr_sum > target or i == len(nums):
                return
            
            backtrack(i+1,curr_sum)

            sol.append(nums[i])
            backtrack(i,curr_sum+nums[i])
            sol.pop()
        
        backtrack(0,0)
        return res