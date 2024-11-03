class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        sol = []
        res = []


        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(sol))
                return

            if openN < n:
                sol.append("(")
                backtrack(openN + 1, closedN)
                sol.pop()
                
            if closedN < openN:
                sol.append(")")
                backtrack(openN, closedN + 1)
                sol.pop()

        backtrack(0, 0)
        return res


solution = Solution()
print(solution.generateParenthesis(n=3))
            
         