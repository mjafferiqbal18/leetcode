class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Problem: 219. Contains Duplicate II
        https://leetcode.com/problems/contains-duplicate-ii/

        Intuition:
        - We see that abs(i-j)<=k -> that puts a bound on the left and right index -> hints at sliding window
        - One could also do a brute force (but O(1) space solution) by comparing pairs of numbers
        - To do a sliding window solution, we need to store the use a set to represent the window

        Time:
        - O(n)

        Space:
        - O(n)

        """
        n=len(nums)
        l=0
        seen=set()

        for r in range(n):
            if nums[r] in seen:
                return True
            seen.add(nums[r])

            if (r-l)==k: #this will break in the next iteration
                seen.remove(nums[l])
                l+=1
        return False

            

        