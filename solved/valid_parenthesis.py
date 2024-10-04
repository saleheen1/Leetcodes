class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stk =[]
        hashData = {")":"(","}":"{","]":"["}

        for v in s:
            if v not in hashData:
                stk.append(v)
            else:
                if not stk:
                    return False
                popped = stk.pop()
                if popped != hashData[v]:
                    return False
                
        return not stk



        
        






s = Solution()
print(s.isValid( s="]"))
            
         