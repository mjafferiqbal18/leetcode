class Solution:
    """
        Problem: 1929. Concatenation of Array
        https://leetcode.com/problems/concatenation-of-array/description/


        Intuition:
        - Copy over the original nums, iterate over it and append to it
        
        Time Complexity:
        - O(n)

        Space Complexity:
        - O(2n) -> O(n)
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=nums.copy()
        for n in nums:
            res.append(n)
        return res