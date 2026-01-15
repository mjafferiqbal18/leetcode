class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Problem: 153. Find Minimum in Rotated Sorted Array
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

        Intuition:
        - We can find min in O(n) time, but we need to do it in logn -> binary search
        - Binary search requires sorted input / monotonicity, but if rotated, then there can be monotonicity in atleast one half
            - we can then prune that side
        - if st<end, its not rotated, return st
        - else check mid:
            - if mid>st: minimum must be to the right of mid -> thats incorrect, because st could be min too
            Then, the correct condition is to check mid and end:
            - if mid<end:
                - that means right half is sorted, and minimum could be st..mid inclusive
            -  else: (mid>end):
                - that means left half is sorted (but minimum is somewhere in right side as that side breaks monotonicity)
                - min could be mid+1..end inclusive
        - we continue loop until st<end, not st<=end: 
            - We're eliminating a half based on the two conditions
            - but if mid==end:
                - that means we are evaluating one candidate (and have eliminated the rest of the array) -> that must be minimum
        - at the end, minimum should be nums[st] or nums[end]
            - the loop ends when st==end, so either way, we have found the minimum (you can return either one)
        
        Time:
        - O(logn)

        Space:
        - O(1)
        """
        st=0
        end=len(nums)-1

        while st<end:
            mid= (st+end)//2
            if nums[mid] < nums[end]: # right is sorted, min could be from st..mid inclusive
                end=mid
            else: #right is not sorted, min could be from mid+1..end
                st=mid+1
        return nums[st]
        
        """

        We need to find pivot, (where nums[x]<nums[x+1] OR nums[x]<nums[x-1])
        - if st < end -> then not rotated -> return st (which is min)
        - else:
            - if mid (or mid-1 or mid+1) is pivot and return that
            - else we need to go to a half:
                - if mid>st (and hence mid>end) -> go right because left is sorted
                - else -> go left because right is sorted (because for left half, st>mid)

        We make cases:
        r=0 | [1,2,3,4,5] | case A
        r=1 | [5,1,2,3,4] | case B
        r=2 | [4,5,1,2,3] | case C
        r=3 | [3,4,5,1,2] | case D
        r=4 | [2,3,4,5,1] | case E
        r=5 | [1,2,3,4,5] | case F

        we can see if st<end then it must not be rotated (r=0 or 5)
        then we look at midpoint to find pivot:
        - if mid<mid-1 (as in case C), then we know we have found the min
        - if mid>mid+1 (as in case D), then we know we have found the min
        - else, we must choose to go left or right:
            - left if mid is greater than both st and end
            - right if mid is less than both st and end
            - all other cases are handled by the prior cases
        """
        l=len(nums)
        if l<3:
            return min(nums)
        
        st=0
        end=l-1
        
        if nums[st]<nums[end]:#not rotated
            return nums[st]
        
        while st<=end:
            mid=(st+end)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid]>nums[st] and nums[mid]>nums[end]:#go right
                st=mid+1
            elif nums[mid]<nums[st] and nums[mid]<nums[end]:#go left
                end=mid-1
        
        return -1


