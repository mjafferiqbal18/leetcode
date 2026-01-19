class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Problem: 410. Split Array Largest Sum
        https://leetcode.com/problems/split-array-largest-sum/

        Intuition:
        - When we split, the largest sum can range from max(nums) to sum(nums)
        - Since this is a LIMITED RANGE and MONOTONICALLY INCREASING, we can run binary search on it
            - To check if a largest sum is valid, we try to see how many subarrays we require, such that the sum of a subarray never exceeds a the 'largest' candidate value
            - if the number of subarrays required is <= k, then this is a valid largest number
                - if valid, we decrease the range
                - if invalid, that means we need to increase the largest candiate number
        
        Time:
        - O(nlog(sum(nums)))

        Space:
        - O(1)

        regardles of if k is 2 or 3 or more
        the max sum of a subarray (theoretically, not practically) would be sum(nums)
        the minimum sum of a subarray would be max(nums)
        we can run binary search from max(nums) to sum(nums)
        we validate the mid value by checking if that mid value is a valid solution, make it solution so far, and continue
        Time= n*log(sum)

        """

        l,r= max(nums),sum(nums)
        res=r

        while l<=r:
            mid=l+((r-l)//2)    #mid=(l+r)//2 is fine, may lead to overflow
            if self.canSplit(mid,nums,k):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
    
    def canSplit(self,largest,nums,k):
        """
        This function checks if we can split the array into <=k subarrays, such that the sum of a subarry never exceeds largest
        """
        subarrays=0
        currSum=0

        for n in nums:
            currSum+=n
            if currSum>largest:
                subarrays+=1
                currSum=n
        subarrays+=1 #because we only added 1 if we needed to create a second one
        return subarrays<=k #this works because if all the elems can be in 2 subarrays, and m is 3, then all elements can be in 3 subarrays where max total is less than largest 

    """
    Backtracking solution with memoization!
    Time=O(k*n^2) -> k*n states, and at each state we go to end of the list

    Though subarray is contiguous so we dont need backtracking solution generally

    """
    def splitArray2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[-1] * (k + 1) for _ in range(n)] #dp is states of i,m -> represents the minimum sum of largest subarray formed from index i and onwards, where you have to form k subarrays

        def dfs(i, m):
            if i == n: #we reached the end
                return 0 if m == 0 else float("inf") #if we formed exactly m subarrays, this is a valid solution
            if m == 0: #if elems left, but cant form more subarrays, invalid solution
                return float("inf")
            if dp[i][m] != -1:
                return dp[i][m]

            res = float("inf")
            curSum = 0 
            #We are at i, and we need to create m subarrays out of nums[i:].
            #Let’s pick the first subarray to be nums[i..j] (inclusive).
            #Then the rest (nums[j+1..]) must be split into m-1 subarrays.
            for j in range(i, n):
                curSum += nums[j]
                res = min(res, max(curSum, dfs(j + 1, m - 1)))

            dp[i][m] = res
            return res

        return dfs(0, k)