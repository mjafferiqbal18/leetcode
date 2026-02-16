class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Problem: 287. Find the Duplicate Number
        https://leetcode.com/problems/find-the-duplicate-number/

        Hated this questions through and through

        Intuition:
        We frame this as a linked list containing a cycle
         0,1,2,3,4
        [1,3,4,2,2] -> nums are values and point to next idx 
        there can be no cycle at start because no elem can point to idx 0 (since range is 1-n)
        1 -> 3 -> 2 -> 4 
                  \ <- /  

        Use Floyd's algo to solve (SEE PROOF FROM NEETCODE VIDEO. IMPORTANT!!!)
        - Find point at which fast and slow ptr meet (ptr A)
        - Move head and ptr A one step until they meet -> this is the start of the cycle
        - Start of cycle is the duplicate number (2 in above example)
        
        Benefit of this is that it can be done in O(1) space
        """
        slow,fast=0,0
        while 1:
            slow = nums[slow] #move 1 step =, i.e. go to idx pointed to by currnum
            fast = nums[nums[fast]] #move 2 steps

            if slow==fast:
                break
        slow2=0 #initialize at head
        while 1:
            slow2=nums[slow2]
            slow=nums[slow]
            if slow==slow2:
                break
        return slow


        