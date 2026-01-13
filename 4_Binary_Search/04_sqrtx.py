class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Problem: 69. Sqrt(x)
        https://leetcode.com/problems/sqrtx/

        Intuition:
        - We want to find y (within the range 0..x) such that y*y==x
        - Since y needs to be an int, we need to find the largest y such that y*y <=x and y*y is closest candidate to x
        - Simple binary search applicable
        - At the end when we dont find a whole num sqrt (when l and r cross):
            - r is the largest value < than target
            - l is the smallest value > target

        Time:
        - O(logn)

        Space:
        - O(1)

        """
        l,r=0,x
        largest=0
        while l<=r:
            mid=(l+r)//2
            if mid*mid>x:
                r=mid-1
            elif mid*mid<x:
                largest=max(largest,mid)
                l=mid+1
            else:
                return mid
        # return largest
        return r
