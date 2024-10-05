class Solution:
    def recursion(self, k: int) -> list[str]:
        
       def recursion(n):
           if n==1:
               return n
           print(n)
           return recursion(n-1)
       
       recursion(n=5)





solution = Solution()
print(solution.recursion(k=3))
            
         