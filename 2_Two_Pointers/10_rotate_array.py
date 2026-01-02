class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Problem: 189. Rotate Array
        https://leetcode.com/problems/rotate-array/

        Intuition:
            - A brute force way would break the in-place constraint (by building a new result)
            - To do it inplace, one can think of the following:
                - e.g. [1,2,3,4,5], k=2 -> [4,5,1,2,3]
                - First we reverse the complete array: [5,4,3,2,1]
                - Then individually reverse the components:
                    - [5,4,3,2,1] -> [4,5,3,2,1] -> [4,5,1,2,3]

        Reverse input array, and then reverse first k elems, and then the res

        """
        n=len(nums)
        if n==1:
            return nums
        
        k=k%n #to make sure k is bounded 1..n
        #reverse full
        l,r=0,n-1
        self.rev(l,r,nums,n)
        
        #now reverse first k elems
        l,r=0,k-1
        self.rev(l,r,nums,n)

        #now reverse the rest
        l,r=k,n-1
        self.rev(l,r,nums,n)

    
    def rev(self,l,r,nums,n):
        while l<r and l<n and r<n:
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l+=1
            r-=1
