# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    """
    Problem: 374. Guess Number Higher or Lower
    https://leetcode.com/problems/guess-number-higher-or-lower/

    Intuition:
    - Simple binary search, answer is guaranteed to be in 1..n inclusive

    Time:
    - O(logn)

    Space:
    - O(1)


    """
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            mid=(l+r)//2
            res= guess(mid)
            if res==0:
                return mid
            elif res==1:
                l=mid+1
            elif res==-1:
                r=mid-1
        return -1
        