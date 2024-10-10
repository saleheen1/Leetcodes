class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        left,right,maxProfit = 0,1,0

        while right < len(prices):
            profit = 0
            if   prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit,profit)
            else:
                left = right
            right +=1
                
            
        return maxProfit
    

s = Solution()
print(s.maxProfit(prices=[1,2,4]))




