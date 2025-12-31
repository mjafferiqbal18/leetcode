class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Problem: 75. Sort Colors
        https://leetcode.com/problems/sort-colors/description/

        Intuition:
        - We could implement merge-sort for an O(logn) solution
        - Since the range of values is limited, we can use a bucket-sort solution
        - In each bucket, the value will be the same, so we can store a counter for that (instead of storing values)
        - This guarantees a 2 pass linear time solution!

        Time Complexity:
        - O(n)

        Space Complexity:
        - O(1)

        """
        bucket=[0]*3 #bucket idxs are 0,1,2
        for num in nums:
            bucket[num]+=1 
        
        c=0
        for i in range(3):
            for j in range(bucket[i]):
                nums[c]=i
                c+=1
       

        