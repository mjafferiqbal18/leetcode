class Solution:
    """
        Problem: 242. Valid Anagram
        https://leetcode.com/problems/valid-anagram/description/


        Intuition:
        - Anagrams have the same count of characters they contain
        - Build a dictionary of character count, and compare at the end
        - Alternatively, sort in nlogn time, and compare in a linear pass
        
        Time Complexity:
        - O(n)

        Space Complexity:
        - O(n) 
    """
    def isAnagram1(self, s: str, t: str) -> bool:
        """
        Uses counter -> also O(n) but fastest because optimzed for counting elements
        in an iterable
        """
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Using separate Dicts with early termination
        Time: O(s+t), Space: O(s+t)
        """
        charCountS={}
        charCountT={}

        if len(s) != len(t): #early termination
            return False
        
        for character in s:
            if charCountS.get(character):
                charCountS[character]+=1
            else:
                charCountS[character]=1
        
        for character in t:
            if not charCountS.get(character): #if that character does not exist in s
                return False
            
            if charCountT.get(character):
                charCountT[character]+=1
                if charCountT[character]>charCountS[character]: #if count of character in t > count of character in s, terminate
                    return False
            else:
                charCountT[character]=1 
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        Uses sorting 
        Time: nlog(n) Space: O(1) for some sorting algos otherwise O(n)
        in Practice not good 
        """
        return sorted(s) == sorted(t)




