class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Problem: 18. 4Sum
        https://leetcode.com/problems/4sum/

        Intuition:
            - Same thing as threeSum, but with another extra outer for loop (ensuring no duplicates by picking a nums[i]!=nums[i-1])
            - Introducing loop after loop is hardcoded, especially if we try to generalize to k-sum
            - Instead, use recursion:
                - base case would be if k=2, in which we would provide a target and do regular 2sum
                - recursive case would be if k>2:
                    - we would iterate from a startIdx to n-kth idx (in range we would provide n-k+1) (eg, if k=3, n=5, then we can use idx=0,1,2,3 as the current elem)
                    - we will also make sure to skip any duplicates: if i>startIdx and nums[i]==nums[i-1], then continue
                    - since you need to return the complete triplets, youll perform a backtracking style append and pop to res

        Time:       
        - O(n^(k-1))
        
        Space:
        - O(1)

        """
        nums.sort()
        n=len(nums)
        res=[]
        quad=[]

        def kSum(k,startIdx,target):
            if k!=2:
                for i in range(n-k+1): #iterate from start till last k-1 vals
                    #ensure you dont pick the same value for this position again
                    if i>startIdx and nums[i]==nums[i-1]:
                        continue
                    #put this element into a temporary store
                    quad.append(nums[i])
                    #recurse on k-1, a startidx that is +1 currIdx, and reduce the target by currNum
                    kSum(k-1,startIdx+1,target-nums[i])
                    #now, we can 'backtrack', i.e. pop this
                    quad.pop()
                return
            
            l,r=startIdx,n-1
            while l<r:
                twoSum=nums[l]+nums[r]
                if twoSum>target:
                    r-=1
                elif twoSum<target:
                    l+=1
                else:
                    res.append(quad+[nums[l],nums[r]])
                    l+=1
                    while l<n and nums[l]==nums[l-1]: #ensure we dont pick the same l again to avoid duplicates
                        l+=1
        kSum(4,0,target)


        """
        Hard-coded 4-sum
        """
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and j<n and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=n-1
                twosum=nums[i]+nums[j]
                while l<r:
                    foursum= twosum+nums[l]+nums[r]
                    if foursum>target:
                        r-=1
                    elif foursum<target:
                        l+=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    
        return res

                 
        