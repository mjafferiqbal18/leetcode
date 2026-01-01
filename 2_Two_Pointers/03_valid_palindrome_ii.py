class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Problem: 680. Valid Palindrome II
        https://leetcode.com/problems/valid-palindrome-ii/
        
        Intuition:
        - Same thing as Valid Palindrome 1 (except for cleaning the string part)
        - Use a bool to track deletion
            - for the first mismatch, just set the bool 
                - now question is which pointer to decrement
                - we decrement l, check remaining, then decrement right, check remaining
            - for subsequent mismatches, you can return False
        
        Time:
        - O(n)

        Space:
        - O(1)
        """
        deleted=False
        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                if not deleted:
                    deleted=True
                    #can not consider either s[l] or s[r]
                    return self.checkPali(l+1,r,s) or self.checkPali(l,r-1,s)
                else:
                    return False
            l+=1
            r-=1
        return True
    def checkPali(self,l,r,s):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        