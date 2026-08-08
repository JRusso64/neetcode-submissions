class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1

        res = 0
        while r < len(prices):
            res = max(prices[r] - prices[l], res)
            if prices[l] > prices[r]:
                l=r
                r+=1
            else:
                r += 1
            
        return res