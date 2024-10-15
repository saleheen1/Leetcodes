class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        xString = str(x)
        left = 0
        right = len(xString) -1

        while left <= right:
            if xString[left] == xString[right]:
                left +=1
                right -=1
                continue
            return False
        return True

solution = Solution()
res = solution.isPalindrome(x=1213)
print(res)
