class Solution:
    """
    Problem: 88. Merge Sorted Array
    https://leetcode.com/problems/merge-sorted-array/

    Intuition:
    - We need to use two pointers, however merging from start risks breaking the sorting order (e.g. you swap an elem from nums1 to nums2, which then breaks the sorting order of nums2)
    - We know that nums1 has empty space at the end, so we can sort via descending order, and we wont be risking breaking sorting orders
    - Dont forget leftover elements (handle at end)

    Time:
    - O(n)

    Space:
    - O(1)
    
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        If you want to do in place, start i=m+n-1 (because there is empty space)
        Then you can sort via descending order

        if you start at start of both and replace num1s at start you risk breaking sorting order of either

        """
        last=m+n-1
        
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1
        #fill nums1 with leftover nums2elems
        while n>0:
            nums1[last]=nums2[n-1]
            n-=1
            last-=1
        
        
            

       

        