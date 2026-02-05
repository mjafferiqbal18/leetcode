class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Problem: 424. Longest Repeating Character Replacement
        https://leetcode.com/problems/longest-repeating-character-replacement/

        Intuition:
        - Instead of keeping exact track of counts of a specific char in a window, think of it like this:
        - In a window (size=r-l+1), k should be <= (windowSize - countOfMostFreqCharInWindow)
        - as long as [(windowSize - countOfMostFreqCharInWindow)<=k], length of window is substring formed
        - This ensures that we don't keep track of chars and counts, only need to satisfy the equation!
        - we need to maximize the valid window size
        
        PS: When shifting window by incrementing l, remove its count from the window too
        
        Time:
        - O(26*n)=n

        Space:
        - O(26)
        
        https://www.youtube.com/watch?v=tkNWKvxI3mU 
        """
        maxCount=0
        windowCounts=[0]*26
        l=0

        for r in range(len(s)): #go over possible r's (0 to len-1)
            windowCounts[ord(s[r])-65]+=1 #we have seen s[r], so update count
            
            while ((r-l+1)-max(windowCounts)) > k: #(windowSize - countOfMostFreqCharInWindow) if >k
                windowCounts[ord(s[l])-65]-=1 #decrement the count of the char at l
                l=l+1 #shift left end of the window
            
            maxCount=max(maxCount,(r-l+1))
        
        return maxCount