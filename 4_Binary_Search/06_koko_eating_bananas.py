class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Problem: 875. Koko Eating Bananas
        https://leetcode.com/problems/koko-eating-bananas/

        Intuition:
        - We know that the range is 1...max_of_pile (this is potential k)
        - In brute force, we can can each num to see if its a valid solution (i.e. if we can finish the pile in <= h hours) -> O(max(p)*p)
        - Since we know the range:
            - 1...max_of_pile
            - We can see monotonicity 
            - We can then use a binary search
            - Use a helper to tell you the hours taken to finish all piles, given a candiate k
                - Helper iterates over each pile, adds ceil(pile/k) to hours

        Time:
        - O(p log(max(p))) where p is the number of piles

        Space:
        - O(1)

        """
        maximum=max(piles)

        #early termination
        if h==len(piles): 
            return maximum
        
        st=1
        end=maximum
        res=maximum
        while st<=end:
            potentialK=(end+st)//2
            hoursToFin=self.hoursToFinishPile(piles,potentialK)
            if hoursToFin<=h: #search on left half
                res=min(potentialK,res)
                end=potentialK-1 
            else:
                st=potentialK+1 #bec hours taken to fin was > h, so we need to try a bigger k
        return res

    def hoursToFinishPile(self,pile:List[int],k:int) -> int:
        hoursTaken=0
        for p in pile:
            hoursTaken+=ceil(p/k)
        return hoursTaken

    