from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for v in word:
                count[ord(v) - ord('a')] +=1
            
            res[tuple(count)].append(word)
        return res.values()


            

s = Solution()
print(s.groupAnagrams(strs=["act","pots","tops","cat","stop","hat"]))