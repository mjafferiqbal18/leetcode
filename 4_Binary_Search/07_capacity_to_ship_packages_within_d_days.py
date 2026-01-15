class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Problem: 1011. Capacity To Ship Packages Within D Days
        https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

        Intuition:
        - We cant split a package across days
        - Minimum capacity of ship can be max(weights), so every package can be loaded onto the ship
        - Maximum capacity of the ship can be sum(weights), so all packages can be loaded on the same day
        - We have a min/max range here (the numbers are sorted in this range), so we can think of a binary search solution
            - At each candidate capacity, we can traverse the array in O(n) and see if all packages can be loaded within d days
            - everytime loadedWeight>cap, you increase the number of days required, and make loadedWeight=last weight (this is loaded on the next day)
        - In the binary search, we record max valid cap
        
        Time:
        - O(nlog(sum(cap)-max(cap)))

        Space:
        - O(1)
        
        """

        st,end=max(weights),sum(weights) #you could have max cap of sum, so everything loaded on one day
        #min cap would be the max weight, so that atleast every weight can be loaded on one day
        minCap=end
        while st<=end:
            mid=(st+end)//2
            if self.canShip(weights,mid,days): #we can ship
                minCap=min(minCap,mid)
                end=mid-1
            else:
                st=mid+1
        return minCap

    def canShip(self,weights,cap,days):
        requiredDays=0
        currLoad=0

        for weight in weights:
            currLoad+=weight
            if currLoad>cap:
                requiredDays+=1
                currLoad=weight
        return (requiredDays+1)<=days

        