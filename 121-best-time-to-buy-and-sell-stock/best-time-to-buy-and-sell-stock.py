class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l=0
        r=l+1
        maxprofit=0

        while r<len(prices):
            if prices[l]<prices[r]:
                maxprofit=max(maxprofit,prices[r]-prices[l])

            else:
                l=r
            
            r+=1

        return maxprofit
        