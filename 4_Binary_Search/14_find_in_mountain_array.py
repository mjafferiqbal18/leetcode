# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    """
    Problem: 1095. Find in Mountain Array
    https://leetcode.com/problems/find-in-mountain-array/

    Intuition:
    - We can always find a target in an array in a linear fashion; since we need to minimize operations, we need to run binary search
    - Monotonic property does not hold because of the mountain, but:
        - idx 0 -> peakIdx is in increasing order
        - idx peak -> idx n-1 is in decreasing order
    - We can find the peak idx using binary search, then run increasing binary search on left half and decreasing on right half
        - to find peak idx, we try midVal, update current peak
        - if mountainArr.get(mid-1)>mid, it means we need to search left half for peak, otherwise we need to search right half for pea
    
    Time:
    - O(logn)

    Space:
    - O(1)

    """
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        lenMountainArr=mountainArr.length()
        l,r=0,lenMountainArr-1
        peak=0
        peakIdx=-1

        #finding the peak
        while l<=r:
            mid=(l+r)//2
            midVal=mountainArr.get(mid)
            if midVal>peak:
                peak=midVal
                peakIdx=mid
            if mid-1>=0 and mountainArr.get(mid-1)>midVal: #peak is on the left side
                r=mid-1
            else: #peak is on the right side
                l=mid+1
        
        #check if peak is target
        if target==peak:
            return peakIdx
        
        #check left side of the peak - this is in increasing order
        l,r=0,peakIdx-1
        while l<=r:
            mid=(l+r)//2
            midVal=mountainArr.get(mid)
            if midVal>target: #go left
                r=mid-1
            elif midVal<target: #go right
                l=mid+1
            else:
                return mid
        
        #check right side of peak - this is in decreasing order
        l,r=peakIdx+1,lenMountainArr-1
        while l<=r:
            mid=(l+r)//2
            midVal=mountainArr.get(mid)
            if midVal>target: #go right
                l=mid+1
            elif midVal<target: #go left
                r=mid-1
            else:
                return mid
        
        return -1

   
        
          