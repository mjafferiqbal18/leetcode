class Solution:
    """
        Problem: 1. Two Sum
        https://leetcode.com/problems/two-sum/description/

        Intuition:
        - x + y = z; if you have seen y, you want to know if you have seen (z-y) before
        - if there is a z-y = x, then we have a valid two sum
        
        Time Complexity:
        - O(n)

        Space Complexity:
        - O(n) 
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Trick -> think of problem as finding the complement of a num
        Time: O(n) Space: O(n)
        n+c=target, c=target-n
        """
        idxDict={}
        for idx,n in enumerate(nums):
            # c=target-n
            if (target-n) in idxDict: #if complement exists
                return [idx,idxDict[target-n]]
            else:
                idxDict[n]=idx

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        First sort -> O(nlogn)
        Build num to idxDict -> O(n)
        Do two pointer pass -> O(n)
        Time: O(nlogn)
        """

        sortedNums =sorted(nums)
        lenNums=len(nums)
        idxDict={}
        for idx,n in enumerate(nums):
            if idxDict.get(n):
                idxDict[n].append(idx)
            else:
                idxDict[n]=[idx]

        start=0
        end=lenNums-1
        while start != end:
            if (sortedNums[start]+sortedNums[end]) == target:
                if sortedNums[start] == sortedNums[end]:
                    return [idxDict[sortedNums[start]][0],idxDict[sortedNums[end]][1]]
                else:
                    return [idxDict[sortedNums[start]][0],idxDict[sortedNums[end]][0]]
            elif (sortedNums[start]+sortedNums[end]) > target:
                end-=1
            elif (sortedNums[start]+sortedNums[end]) < target:
                start+=1
        return None
    
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force -> O(n^2)
        """
        for idx1, n in enumerate(nums):
            for idx2,nPrime in enumerate(nums):
                if idx1!=idx2 and (n+nPrime==target):
                    return [idx1,idx2]
        return None



        