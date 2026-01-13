class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Problem: 704. Binary Search
        https://leetcode.com/problems/binary-search/

        Intuition:
        - Nothing lol, simple binary search

        Time:
        - O(logn)

        Space:
        - O(1)
        """
        st=0
        end=len(nums)-1
        while st<=end:
            idx=(end+st)//2 #can alternatively do st+(end-st)//2
            if nums[idx]>target:
                end=idx-1
            elif nums[idx]<target:
                st=idx+1
            else:
                return idx
        return -1

            
            
                