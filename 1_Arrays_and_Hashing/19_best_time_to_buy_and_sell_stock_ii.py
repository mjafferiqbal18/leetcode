class Solution:
    def __init__(self):
        self.max=0
        self.n=0
    def maxProfit(self, prices: List[int]) -> int:
        """
        Problem: 122. Best Time to Buy and Sell Stock II
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


        Intuition:
        - One could think of an exponential-time backtracking solution (with memoization?) 
            - every index would be buy/sell/do nothing
            - params would be i,canBuy (if youve already bought then you cannot buy)
            - memo [i,canBuy] tells us max profit from i to n-1, if you land at i with canBuy=canBuy
            - This would also be a linear-time memo (and thus a linear time solution), because memo would be of size 2n=O(n)

        - Optimal: to maximize profit, we can try capturing every upward slope in prices
            - the sum of the local upward slopes = the biggest upward slope possible between two points
                - for example: [1,2,3,4,5], max profit=5-1=4
                    - local positive slopes: (2-1) + (3-2) + (4-3) + (5-4) = 1+1+1+1 = 4

            - with this information, we can try a greedy solution
            - Time=O(n), Space=O(1)
        
        
        """
        n=len(prices)
        b=0 #buy idx
        s=1 #sell idx
        profit=0
        while s!=n: 
            if prices[s]>prices[b]:
                profit+=prices[s]-prices[b] #capture the local increase in slope
            b=s 
            s+=1
        return profit

        """
        backtracking with memo:
        """
        self.n=len(prices)

        memo={}
        def backtrack(i,haveBought):
            if i==self.n: #max profit from this index forward is 0
                return 0

            if (i,haveBought) in memo:
                return memo[(i,haveBought)]
        
            bestFromHere=0
            if haveBought:
                #sell now (can buy later from this index)
                sellNow= prices[i]+backtrack(i,not haveBought) #backtrack on i, since we can buy again on i

                #not sell right now
                notSellNow= backtrack(i+1,haveBought)

                bestFromHere=max(sellNow,notSellNow)
            else:
                #buy right now
                buyNow= backtrack(i+1,not haveBought) - prices[i]

                #not buy right now
                notBuy= backtrack(i+1,haveBought)
                bestFromHere=max(buyNow,notBuy)
            memo[(i,haveBought)]=bestFromHere
            return bestFromHere

        self.max=backtrack(0,False)
        return self.max
        

        