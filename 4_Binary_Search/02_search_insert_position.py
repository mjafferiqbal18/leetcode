class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Problem: 35. Search Insert Position
        https://leetcode.com/problems/search-insert-position/

        Intuition:
        - best pos to insert is always at the left ptr at the end (nums[l] will be the first element that is >target)
        - At the end:
            - all indices < l are < target
            - all indices > r are > target
            - But when l > r, there is no index between them anymore
            - At the end, l becomes: The index of the first element ≥ target, or len(nums) if no such element exists.
        """
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else: #nums[mid]==target
                return mid
        return l
        