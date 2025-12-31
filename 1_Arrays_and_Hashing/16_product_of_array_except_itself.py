class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Problem: 238. Product of Array Except Self
        https://leetcode.com/problems/product-of-array-except-self/

        Intuition:
        - Brute force solution would require a linear scan per element, hence be in quadratic time
        - We could use prefix[i] (prod of elements 0..i-1) and postfix[i] (prod of elements i+1..n-1)
        - Building a prefix/postfix array would require 0(n) space, apart from the resulting output array
        - You could keep a running product and fill in the products into the resulting array in 2 passes, requiring only O(n) space for res, and constant for rest

        Time Complexity:
        - Brute force: for each element, traverse whole array -> O(n^2)

        - Current sol:
            - Time: 2n -> O(n)
            - Space: 1 (apart from output array) -> O(1)
        """
        len_nums=len(nums)
        res=[1]*len_nums
        runningProduct=1
        #forward pass
        for i in range(len_nums):   
            if i!=0:
                runningProduct*=nums[i-1]  
            res[i]*=runningProduct   
        
        runningProduct=1
        #backward pass
        for i in range(len_nums-1,-1,-1):
            if i!=len_nums-1:
                runningProduct*=nums[i+1]
            res[i]*=runningProduct

        return res
    

    def productExceptSelf_Neetcode(self, nums: List[int]) -> List[int]:
        """
        backward pass:  -> O(n)
        forward pass: -> O(n)
        we will have a variable to store forward pass count and backward pass count
        No need for separate arrays
        """
        lenNums=len(nums)
        res=[1]*lenNums  
        prefix= 1
        
        for i in range(lenNums): #forward pass
            res[i]=prefix 
            prefix*=nums[i] #=prefix*myself
        
        postfix=1
        
        for i in range(lenNums-1,-1,-1): #backward pass
            res[i]*=postfix
            postfix*=nums[i] 
        
        return res

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        """
        backward pass:  -> O(n)
        [1,2,3,4] | [1,1,1,1]
        [24,12,4,1]

        forward pass: -> O(n)
        [1,2,3,4] | [1,1,1,1] | [24,12,4,1]
        [1,1,2,6] | 
  
        element-wise multiplication -> O(n)
        [24,12,4,1]
        [1,1,2,6]

        Answer: [24,12,4,1]
        """
        lenNums=len(nums)
        resForward=[1]*lenNums
        resBack=[1]*lenNums
        res=[0]*lenNums  
        idx=lenNums-1 #3
        
        # for i in range(idx,0,-1):
        #     resBack[i-1]*=(nums[i]*resBack[i])
        # for j in range(0,idx):
        #     resForward[j+1]*=(nums[j]*resForward[j])

        for i in range(idx,0,-1): #mashing the two for loops above into one
            resBack[i-1]*=(nums[i]*resBack[i])
            resForward[idx-i+1]*=(nums[idx-i]*resForward[idx-i])

        for k in range(lenNums):
            res[k]=resForward[k]*resBack[k]
        return res



        




    