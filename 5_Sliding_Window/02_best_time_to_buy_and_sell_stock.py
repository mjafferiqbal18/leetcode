class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Problem: 121. Best Time to Buy and Sell Stock
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

        Intuition:
        - You can use two pointers: every time prices[r]<prices[l], make l=r, and shift r too
        - This should ensure you capture the minimum of the pairs in left, and anything bigger with r
        """

        n= len(prices)
        l,r = 0,1
        profit = 0

        while r < n:
            if prices[r]<prices[l]:
                l=r
            else:
                profit = max(profit, prices[r]-prices[l])
            r+=1
        return profit
            

        