class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Problem: 1768. Merge Strings Alternately
        https://leetcode.com/problems/merge-strings-alternately/

        Intuition:
        - Initialize ptrs at start of both strings
        - Lesson: you're merging 2 strings, so you'd run the loop util either ptr is out of bounds
        - Finally, merge the remaining string

        Time:
        - O(n) where n is length of longer string

        Space:
        - O(n+m)
        
        """
        w1=0
        w2=0
        res=""

        while w1<len(word1) and w2<len(word2):
            res+=word1[w1]
            w1+=1
            res+=word2[w2]
            w2+=1
        if w1<len(word1):
            res+=word1[w1:]
        elif w2<len(word2):
            res+=word2[w2:]
        return res        