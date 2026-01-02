class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Problem: 881. Boats to Save People
        https://leetcode.com/problems/boats-to-save-people/

        Intuition:
        - Logically, a person with the most amount of weight needs to be paired up with a person with less weight
        - We can terminate early if any single person's weight is more than limit
        - We sort, and initialize ptrs r and l
        - If people[l]+people[r]>limit, that means people[r] can only stay on the boat, we decrement people[r]
        - If people[l]+people[r]<=limit, then we put them on the boat, and push l and r inwards

        Time: 
        - O(nlogn) because of sorting

        Space:
        - O(1)

        limit=5
        [1,2,2,3] limit=3
        """
        people.sort()
        n=len(people)
        l,r=0,n-1
        boatCount=0
        while l<=r:
            if people[l]+people[r]>limit:
                boatCount+=1
                r-=1
            else:
                boatCount+=1
                r-=1
                l+=1
        return boatCount



        