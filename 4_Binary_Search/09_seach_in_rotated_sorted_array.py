class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Problem: 33. Search in Rotated Sorted Array
        https://leetcode.com/problems/search-in-rotated-sorted-array/

        Intuition:
        If array is sorted but then rotated, some half is bound to be sorted
        - if st or end or mid == target, return the idx
        - else we need to go to a half:
            - if left half sorted:
                - if target in left half, go left
                - else go right
            - if right half sorted:
                - if target in right half, go right
                - else go left
        - NOTE: the code assumes that the numbers are distinct!!!

        You can also ONLY check if mid=target, and make other bounds inclusive (i.e. <= instead of <)
        If you check  st or end or mid == target, then make the other bounds and comparisons strict (< instead of <=)

        Time:
        - O(logn)

        Space:
        - O(1)
        """
        l=len(nums)
        st=0
        end=l-1
        
        while st<=end:
            mid=(st+end)//2
            # if nums[st]==target:
            #     return st
            # elif nums[end]==target:
            #     return end
            if nums[mid]==target:
                return mid
            
            #now we need to go to one half of the array
            if nums[st]<=nums[mid]:#left half is sorted 
                #st could be equal to mid (and thus sorted) so we need to check nums[st]<=nums[mid]
                if target>=nums[st] and target<nums[mid]: #target is in left half
                    end=mid-1
                else:
                    st=mid+1
            else:#right half is sorted
                if target>nums[mid] and target<=nums[end]: #target is in right half
                    st=mid+1
                else:
                    end=mid-1
        return -1
        
