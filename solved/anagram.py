class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        sDict = {}
        tDict = {}

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i],0) + 1
            tDict[t[i]] = tDict.get(t[i],0) + 1
            
        
        for k in sDict:
            if sDict[k] != tDict.get(k, 0):
                return False
                
        return True

        

        

s =Solution()
print(s.isAnagram(s="a",t="ab"))