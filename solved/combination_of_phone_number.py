class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "": return []
        res,sol = [],[]
        hashData = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        def backtrack(i):
            if i == len(digits):
                res.append("".join(sol))
                return

            for v in hashData[digits[i]]:
                    sol.append(v)
                    backtrack(i+1)
                    sol.pop()
        
        backtrack(0)
        return res