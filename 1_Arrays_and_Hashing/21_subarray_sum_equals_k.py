class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Problem: 560. Subarray Sum Equals K
        https://leetcode.com/problems/subarray-sum-equals-k/

        Intuition:
        - A brute force (quadratic time) solution would be to find all subarrays and check if sum=k
        - For linear time, the problem can be solved in a way similar to two sum
            - As we iterate we have a running sum, which we store in a prefix arr, where prefix[i]=sum of elements 0..i (including i)
            - if runningSum-k exists in the set of seen prefixes, that means that there exists a subarray with sum=k. We increment res
            - Note, we could have multiple subarrays with the same prefix (can happen due to negative numbers too), so its better to have a map (prefix->count) instead of a set, and increment res by count

        
        Naive sol is O(n^2), we want to try for O(n) [WATCH NEETCODE VIDEO!]

        [. . . . * . . . .]
        When we are at *, there are 5 possible subarrays with * at the end -> ['. . . . *', '. . . *', '. . *', '. *', '*']
        Prefix sum at * = x = . + . + . + . + * 
        For the sum of A SUBARRAY OF * TO BE EQUAL TO K, you need to have seen a prefixSum of x-k
        So, the number of subarrays of * with sum=k is the number of prefixes you see which are equal to x-k
     
        https://www.youtube.com/watch?v=xvNwoz-ufXA

        How to come from naive solution to optimal solution:
        In naive solution, for iteration i, we need to visit all _ 
            [ . . . . * . . . ]
        i=0 [ _ _ _ _ _ _ _ _ ]  
        i=1 [ . _ _ _ _ _ _ _ ]  
        i=2 [ . . _ _ _ _ _ _ ]  
        i=3 [ . . . _ _ _ _ _ ]  

        Across iterations, we see a lot of repeated work, which can be somehow avoided using prefixes
        """
        prefixMap={0:1}
        res=0
        prefix=0
        
        for n in nums:
            prefix+=n
            if (prefix-k) in prefixMap:
                res+=prefixMap[prefix-k]
            if prefix in prefixMap:
                prefixMap[prefix]+=1
            else:
                prefixMap[prefix]=1
        
        return res


            




        