class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Problem: 128. Longest Consecutive Sequence
        https://leetcode.com/problems/longest-consecutive-sequence/

        Intuition:
        - Brute force ish: One could sort the array nlogn, then iterate over it (using two pointers) to see if sequence formed
        - A better solution uses a trick:
            - we recognize if we have a set of nums, we can query it in O(1) to check element existence
            - in a linear pass, we can see if a number is the start of a sequence (if its the start of the sequence, the number-1 will not exist)
                - Time= O(n)  -> because each number will be visited at most twice
                - Space=O(n)
        """

        numSet=set(nums)
        longest=0
        for num in numSet:
            if (num-1) not in numSet: #this is start of sequence
                length=0
                while (num+length) in numSet:
                    length+=1
                longest=max(length,longest)
        return longest


        

