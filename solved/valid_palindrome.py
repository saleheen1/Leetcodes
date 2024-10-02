import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newString = re.sub(r'[^a-zA-Z0-9]', '', s)

        rightIndex = len(newString) -1
        leftIndex = 0

        while leftIndex <= rightIndex:
            if newString[leftIndex].casefold() == newString[rightIndex].casefold():
                leftIndex +=1
                rightIndex -=1
            else:
                return False
        return True

            





solution = Solution()
res = solution.isPalindrome(s="Was it a car or a cat I saw?")
print(res)