class Solution:
    def countBits(self, n: int) -> list[int]:
        output = [0]

        for i in range(1, n+1):
            ans = 0
            while i != 0:
                ans +=1
                i = i & (i-1)
            output.append(ans)

        return output