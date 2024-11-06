
class Solution:
    def permucation(self, nums:list[int])->list[int]:
        res,sol = [],[]
        n = len(nums)

        def backTrack():
            if len(sol) == n:
                res.append(sol.copy())
                return
            
            for v in nums:
                if v not in sol:
                    sol.append(v)
                    backTrack()
                    sol.pop()
        
        backTrack()
        return res
