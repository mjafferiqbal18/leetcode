class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Intuition:
        - Since array is sorted, we can use two pointers to code a linear-time O(1) space solution
        - l=0,r=n-1: if sum>target, we need to make the larger number (nums[r]) smaller (so we push r inwards by doing r-=1)
            - the opposite logic is true as well 

        array is sorted, can use two pointers
        Time is O(n) -> just one pass over the array, worse case we need to visit all elements
        Space is O(1) -> not storing anything that grows with n
        """

        l=0
        r=len(numbers)-1

        while l<r:
            if (numbers[l]+numbers[r]) == target:
                return [l+1,r+1] 
            if (numbers[l]+numbers[r])>target:
                r-=1
            elif (numbers[l]+numbers[r])<target:
                l+=1
        return None
        