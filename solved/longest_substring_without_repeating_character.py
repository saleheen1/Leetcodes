class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dataSet = set()
        longestSubstring = 0

        for right in range(len(s)):
            while s[right] in dataSet:
                dataSet.remove(s[left])
                left +=1
            
            dataSet.add(s[right])
            longestSubstring = max(longestSubstring, right -left +1)
            
        return longestSubstring