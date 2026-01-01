class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Problem: 125. Valid Palindrome
        https://leetcode.com/problems/valid-palindrome/

        Intuition:
        - First we need to clean the string (retain only alphanum chars and make everything lowercase)
            - To check if a char is alphanumeric, we could do c.isalnum() [c.isalpha() is for alphabets only]
            - Alternatively, we could ensure that ord(char) is in range ord('a')<=x<=ord('z') (lowercase) OR ord('A')<=x<=ord('Z') OR ord('0')<=x<=ord('9')
        - You could build a cleaned string O(n) space, by appending chars for which c.isAlphaNum()
            - To ensure O(1) space, you could skip chars that are not alphanumeric
        - A palindrome need to read the same forwards and backwards -> s should be equal to reverse(s)
        - We use two pointers l=0,r=n-1 and compare (as long as l<r and s[l] and s[r] are alphanumeric characters)
        
        Time O(n)
        Space O(1)
        """
        start=0
        end=len(s)-1

        while start<end:
            while start<end and not self.isAlphaNumeric(s[start]):
                start+=1
            while end>start and not self.isAlphaNumeric(s[end]):
                end-=1
            if s[start].lower() != s[end].lower():
                return False
            start+=1
            end-=1
        return True
        
    def isPalindrome2(self, s: str) -> bool:
        """
        In efficient as it uses extra memory to build a cleaned string
        but is really fast
        """
        cleanedString=self.cleanString(s)
        lenCleanedString=len(cleanedString)
        if lenCleanedString<=1:
            return True
        
        start=0
        end=lenCleanedString-1

        while start<=end:
            if cleanedString[start]!=cleanedString[end]:
                return False
            else:
                start+=1
                end-=1
        return True
        
        
    def cleanString(self, s:str) -> str:
        """
        make the string lowercase and then remove non-alphanumeric characters using regex
        or python isalnum()
        
        alternatively, filter based on ascii using ord(substring):
        97-122 lowercase
        65-91 uppercase
        48-57 digits
        """
        return ''.join([c.lower() for c in s if c.isalnum()])
        # import re
        # return re.sub(r'[^a-z0-9]', '', s.lower())

    def isAlphaNumeric(self,character:str) -> bool:
        return ((ord('A')<=ord(character)<=ord('Z'))
                or (ord('a')<=ord(character)<=ord('z'))
                or (ord('0')<=ord(character)<=ord('9')))
