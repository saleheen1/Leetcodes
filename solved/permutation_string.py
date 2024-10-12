class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:      
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        
        
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for i in range(n1):
            count_s1[ord(s1[i]) - ord('a')] +=1
            count_s2[ord(s2[i]) - ord('a')] +=1
        
        if count_s1 == count_s2:
            return True
        
        # we need at least n1 length values in count_s2 to check with count_s1
        # After we pass n1 length, if we still didn't find match, we add more to count_s2 and
        # remove the others values which was not a match with count_s1
        for i in range(n1,n2):
            count_s2[ord(s2[i]) - ord("a")]  +=1
            count_s2[ord(s2[i - n1]) - ord("a")] -=1

            if count_s1 == count_s2:
                return True
        
        return False



s =Solution()
print(s.checkInclusion(s1 = "a", s2 = "ab"))