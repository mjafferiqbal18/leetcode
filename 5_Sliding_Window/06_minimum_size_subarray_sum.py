class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Problem: 209. Minimum Size Subarray Sum
        https://leetcode.com/problems/minimum-size-subarray-sum/

        Intuition:
        - You need a contiguous subarray (so a window) such that sum >= target
        - Youd also want a sliding window since we want to minimize the subarray size
        - Naturally youd like to add elems to a window as long as sum is inadequate, and start removing elems once sum is adequate
        - You keep adding elements to the window (i.e. record a running sum which represents the window) (and record the sum) as long as we're less than target
        - The moment you are less than target, youd want to remove elements from the sum, and recording the window size

        Time:
        - O(n)

        Space:
        - O(1)
        """

        n=len(nums)
        minLen=float('inf')
        l=0
        currSum=0
        for r in range(n):
            currSum+=nums[r]
            while currSum>=target and l<=r: #sum >= target
                minLen=min(minLen,r-l+1) #record the window length
                currSum-=nums[l] #reduce the window
                l+=1
        return minLen if minLen!=float('inf') else 0

        