class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Problem: 4. Median of Two Sorted Arrays
        https://leetcode.com/problems/median-of-two-sorted-arrays/

        Intuition:
        - The log(m+n) tells us to use binary search somehow
        - Ideally, the arrays don't overlap (for example, all elems of nums1 are smaller than nums2)
        - Issue is when the arrays overlap.
        - You need to pick x number of elements from nums1, ((m+n)//2 - x) elems from nums2
            - x can range from 0 elements to len(nums1); l=0, r=len(nums1)-1
            - We check if mid is valid:
                - mid is valid if last elements on left are less than first elems on the right
                    - if not (last element of nums1 is bigger, then pick less elems from nums1 to be on the left side)
                             (last element of nums2 is bigger so pick more from nums1, so pick more elems from nums1 to be on the right side)

            NOTE: You can gracefully handle corner cases by keeping default values of float('inf') -> look below
        
        Time:
        - O(log(min(n,m)))

        Space:
        - O(1)

        The goal is to partition both arrays into left and right halves, such that last elems at left <first elem at right
        if m+n=odd, e.g. 13, we need to paritition combined into 6 (x from nums1, y from nums 2 where x+y=6), 7th elem would be median
        or m+n=even, e.g. 12, we need to partition combined into 6, 6th and 7th elem will be used to get median

        if either array can fully come before the other, our job is easy. it is when they overlap thats the issue:

        How to know how many elems to pick from nums1 and how many to pick from nums2?
        Pick SMALLER of nums1 and nums2 and run a binary search
        In this example, m+n=11, we need total 5 elems on right side of imaginary combined array
        nums1= [1,12,14,15]
        nums2= [0,1,2,3,4,9,11]

        pick mid of nums1 (idx=1, so idx0,idx1 chosen, choose 5-2=3 of nums2)
        [1,12] [14,15]
        [0,1,2] [3,4 ...]
        end of nums1[left partition] is bigger than start of nums2[right partition], so we need to pick less of nums1, i.e. choose left part to run remaining binary search

        new mid of nums1 = idx0
        [1] [12,..]
        [0,1,2,3] [4,..]
        valid 

        since odd, we can either pick first of nums1[right part] or nums2[right part] (we take the min)
        if it was even, then we would pick max of (nums1[left part],nums2[right part]) and min(nums1[right part],nums2[right part])
        """

        A,B=nums1,nums2
        if len(nums1)>len(nums2):
            A,B=B,A
        total=len(A)+len(B)
        half=total//2

        l,r= 0,len(A)-1
        #if task is to find kth elem, lo = max(0, k - n) hi = min(k, m), half=k
         
        while 1:
            i=(l+r)//2 #left part of A from 0 to i inclusive
            j=(half-(i+1))-1#left part of B from 0 to j inclusive
            
            # can be out of bounds since while does not enforce l<=r
            Aleft=A[i] if i>=0 else float('-inf') #we do this because we want a default value if i is out of bounds
            Aright= A[i+1] if i+1<len(A) else float('inf') 
            Bleft=B[j] if j>=0 else float('-inf') 
            Bright= B[j+1] if j+1<len(B) else float('inf') 

            if Aleft<=Bright and Bleft<=Aright:
                if total%2>0:#odd
                    return min(Aright,Bright)
                else:#even
                    return ((max(Aleft,Bleft))+(min(Aright,Bright)))/2
            elif Aleft>Bright: #too many from Aleft, use left half
                r=i-1
            else: #we need more from A, so use right half
                l=i+1



            



             
       


        