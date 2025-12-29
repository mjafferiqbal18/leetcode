class Solution:
    """
        Problem: 217: Contains Duplicate
        https://leetcode.com/problems/contains-duplicate/


        Intuition:
        - Build a hash-set of existing elements while iterating
        - If an element exists in the hash-set, then it is a duplicate
        
        Time Complexity:
        - O(n)

        Space Complexity:
        - O(n) 
    """
    def containsDuplicate2(self, nums: List[int]) -> bool:
        """
        Using Set with early termination -> fastest!!!
        Time: O(n), Space: O(n)
        """
        numsCount=set() #set
        for n in nums:
            if n in numsCount:
                return True
            else:
                numsCount.add(n)
        return False 



    