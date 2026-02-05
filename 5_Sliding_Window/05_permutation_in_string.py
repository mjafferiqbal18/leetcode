class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Problem: 567. Permutation in String
        https://leetcode.com/problems/permutation-in-string/

        Intuition:
        - Basic idea is to have a sliding window of len(s1) used on s2
        - We keep sliding the window and comparing window to s1 counts
        - Can use array to represent the counts in window and count of s1 (size=26)
        - Can use a numMatches variable, if numMatches=26 for a window, then return true

        Time:
        - O(len(s2)*26) = O(len(s2))

        Space:
        - O(26)
        """
        s1_len=len(s1)
        s2_len=len(s2)
        if s1_len>s2_len:
            return False
        
        s1Count,s2Count=[0]*26,[0]*26
        for i in range(s1_len):
            s1Count[ord(s1[i])-ord('a')]+=1
            s2Count[ord(s2[i])-ord('a')]+=1
        
        if s1Count==s2Count:
            return True
        
        for i in range(s1_len,s2_len):
            #slide
            s2Count[ord(s2[i-(s1_len)])-ord('a')]-=1 #decrement the char leaving the window
            s2Count[ord(s2[i])-ord('a')]+=1 #increment the char coming into the window
            if s1Count==s2Count: 
                return True
        return False  



        