class Solution:
    def minChange(self, s:str):
        changed_needed = 0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]: changed_needed +=1
        
        return changed_needed