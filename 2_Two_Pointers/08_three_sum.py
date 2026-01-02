class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Problem: 15. 3Sum
        https://leetcode.com/problems/3sum/

        Intuition:
            - Brute force would use 3 for loops: O(n^3)
            - We can cut this down to O(n^2) by utilizing two-sum strategy (AFTER SORTING):
                - a+b+c=target, we can fix a, then use twosum to find a b and c that would sum to target
                - We have to be mindful of duplicates:
                    - Lets say we choose nums[i] to be a
                        - then we choose nums[j] to be b, and nums[k] to be c
                        - we need to ensure that the next nums[j+1] should not be equal to nums[j], because then we would have duplicates in solution
                    - the same logic applies to the 'a' we choose

        Time:
        - O(n^2)

        Space:
        - O(1)       


        O(n^2) solution using target=currNum, use twoPointers to get to target
        Make sure that for a+b+c=0, a does not repeat
        Remove duplicates from final set
        """
        lenNums=len(nums)
        nums.sort()
        res=[]

        for i,n in enumerate(nums):
            #dont use the same 'a' value again for a+b+c
            if i>0 and n==nums[i-1]: 
                continue
            
            l=i+1 #candidate for b
            r=lenNums-1 #candidate for c

            while l<r:
                threeSum=nums[l]+nums[r]+n
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else: 
                    res.append([n,nums[l],nums[r]]) #you dont break here after finding one triplet
                    
                    #imagine [-2,-2,0,2,2] -> even if you just increment l to become 0 sum will become too large and right will be decremented by the code above
                    #since we are placing this check on 'a' above, we do the same for 'b' to avoid duplicates
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
        