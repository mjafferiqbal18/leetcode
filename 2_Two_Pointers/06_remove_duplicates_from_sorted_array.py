class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Problem: 26. Remove Duplicates from Sorted Array
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/

        Intuition:
        - This is very similar to Arrays_and_Hashing/07_remove_element
        - We need to know which element repeats (we can tell that by comparing adjacent elements since array is sorted)
        - Once we know which ones to push to the end of the list, we do that using 2 pointers

        Time:
        - O(n)

        Space:
        - O(n)
        """
        n=len(nums)
        doesRepeat=[False]*(len(nums))

        #populate list
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                doesRepeat[i]=True
        
        l,r=0,0
        while l<n and r<n:
            while r<n and doesRepeat[r]: #keep increasing r ptr until we find a value that does not repeat
                r+=1
            if r>=n: #if r is at end (and we didnt find not repeating value), we return
                break
            #put right val in left
            nums[l]=nums[r]
            l+=1
            r+=1
        return l