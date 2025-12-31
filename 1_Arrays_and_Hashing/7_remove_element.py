class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Problem: 27. Remove Element
        https://leetcode.com/problems/remove-element/

        Intuition:
        - We care about the elems not equal to val (there are k of them) -> we need to arrange them in the first k positions
        - Since we only care about the first k positions, we can swap out elems equal to val to the end of the list -> but its not that easy in practice
        - How would you do this swap? Iterating from i to k-> you'll swap nums[i] (if it equals val) with the first elem from the right that is not val
        - To accomplish this we use a two pointer solution

        Time Complexity:
        - O(n)

        Space Complexity:
        - O(1)
        """
        numVals=0 #num elements that do not equal val, we use this to find k and return that
        for n in nums:
            if n==val:
                numVals+=1 
        
        n=len(nums)
        l,r=0,n-1 #initialize two pointers
        while l<r:
            while r>=0 and nums[r]==val: #we shift it so it points to an element that is not equal to val
                r-=1
            while l<n and nums[l]!=val: #we shift it so it points ot an element that is equal to val
                l+=1
            if l>=r:  #if at any point these pointers cross, we break (that means all k elems at at first k positions)
                break
            #swapping logic
            temp=nums[r]
            nums[r]=nums[l]
            nums[l]=temp
        return n-numVals
        


        