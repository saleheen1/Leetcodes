class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        left = 0
        count = [0]*26

        for right in range(len(s)):
           
            count[ord(s[right]) - 65] +=1
            
            # right - left +1 is giving the window length
            # if we subtract most frequent with window length,
            # we get the characters that needs to be replaced
            while right - left +1 - max(count) > k:
                count[ord(s[left]) - 65] -=1
                left +=1
            
            longest = max(longest,right - left +1)
        
        return longest


s =Solution()
print(s.characterReplacement(s = "AAABABB", k = 1))