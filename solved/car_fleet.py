class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append(float((target - p)) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            
        




s = Solution()
print(s.carFleet(position = [6,8],speed = [3,2],target=10))
            
         