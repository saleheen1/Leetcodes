class Solution:

    def encode(self, strs: list[str]) -> str:
        totalStr = ""
        for i in range(len(strs)):
            totalStr += str(len(strs[i])) + "#" + strs[i]
            
        
        return totalStr

    def decode(self, s: str) -> list[str]:
        i = 0
        res = []
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
                  

s =Solution()
encodedResult = s.encode(strs=['sale','juthi'])
print("encoded: ",encodedResult)
print("decoded " ,s.decode(s=encodedResult))