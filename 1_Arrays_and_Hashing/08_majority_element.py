class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Problem: 169. Majority Element
        https://leetcode.com/problems/majority-element/

        Intuition:
        - There can only be one majority element
        - We count occurence of each elememnt (store in a dict) and then return the one more than majority quantity
        - Boyer-Moore voting algorithm can do this in O(1) space

        Time Complexity:
        - O(n)

        Space Complexity:
        - O(n) since we store the counts
        
        """
        counts={}
        for n in nums:
            if n not in counts:
                counts[n]=0
            counts[n]+=1
        
        maj=len(nums)//2 #a majority element will have count greater than this
        for k,v in counts.items():
            if v>maj:
                return k #since a maj element is guaranteed, this will execute
    
    def boyerMooreVoting(self,nums):
        """
        Intuition:
        - We know a majority element exists; every occurence of the maj element is a +1 vote, and every occurence otherwise is a -1 vote
        - Since element is a majority, it will never get cancelled out
        - We pick a candiate to be a majority element. Every 
        """
        count=0 #votes for candiate
        res=0 #current candiate

        for num in nums:
            if count==0: #we have a fresh candidate
                res=num
            
            count+= 1 if num==res else -1 #once the count gets cancelled out (i.e. becomes 0), we pick a new element to be the candiate
        return res