class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Problem: 41. First Missing Positive
        https://leetcode.com/problems/first-missing-positive/

        Intuition:
        - A brute force solution might be to build a hashset, then iterate from 1 to max(nums), returning the first positive integer not in nums
        - Since O(1) memory is required, we need to somehow use nums as a hashset 
        - Lesson: when O(1) memory required, think of ways to use existing input list to accomplish task
        - During a linear pass, we see num, we can somehow mark nums[num-1] 
            - maybe we can set existing value at nums[num-1] to negative to mark that num-1 exists in the array
            - for this we need to first set all initial (useless) negative values to 0
            - we do a linear pass. for num in nums, we go to idx: num-1 if num-1 is within bounds (>=0 and <n)
                - if nums[num-1] is already negative, do nothing (it is already marked)
                - if nums[num-1] is positive, set the value to negative (now marked)
                - if nums[num-1] is 0, then set the value to a large negative value 
                    - when we later process this large negative value: idxToGoTo= abs(large negative value) -1 
                    - if this value is sufficiently large, it will lead us to out of bounds
                    - this ensures we don't mark a value as existing, when it actually does not
                    - e.g. if we set it to -1, then when processing -1, we set idxToGoTo=abs(-1)-1 = 0 -> we say we have seen the value 1 (by marking idx0) -> making this incorrect
                    - if we set to -(n+1), then abs(-(n+1))-1=n, which is out of bounds
        - Also note, in the worst case, array=[1,2,3,4,5] (so biggest pos would be n+1)

        We know the answer can be between 1...n+1 
        Because worst case, array=[1,2,3,4,5] ans=n+1=6

        We could use a hashset, and loop from 1-->n+1
        Since we want constant memory, we need to use nums as hashset
        nums could represent values from 1...n (where value-1=idx)

        First, set all negative numbers in n=0
        Then at each n, we want to mark we have seen this n
        for each n: 
            take abs(n) and -1 -> this is the idx where you mark 'seen'
            to mark 'seen', set that value to negative of itself
        """
        
        n=len(nums)
        #set existing negative numbers to 0 so they dont interfere
        for i in range(n):
            if nums[i]<0:
                nums[i]=0
        
        for i in range(n):
            val=abs(nums[i]) 
            idxToGoTo=val-1
            if val-1>=0 and val-1<n: #within array bounds
                if nums[val-1]>0:
                    nums[val-1]= -1*nums[val-1]
                elif nums[val-1]==0:
                    nums[val-1]= -1*(n+1) #giving this a big default value
                    # big default value is imp because when we later process this index, 
                    # abs(val)-1=n which will be out of bounds, so we will not be processing it per se

        #now we iterate over our range
        for i in range(1,n+1):
            if nums[i-1]>=0: 
                return i
        return n+1
