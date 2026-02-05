class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Problem: 3. Longest Substring Without Repeating Characters
        https://leetcode.com/problems/longest-substring-without-repeating-characters/


        Intuition:
        - Keep adding to set, the moment you get an elem already in set, you reduce you window until that prev elem is gone

        Time:
        - O(n)

        Space:
        - O(n)

        Neetcode solution for sliding window, conceptually same as mine, but simpler code
        """
        charSet=set()
        l,res=0,0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) #removes from the left
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res

    def lengthOfLongestSubstringMine(self, s: str) -> int:
        """
        Our solution has the same basic idea as the sliding window, where our seen_dict keeps tract of the window

        Should take O(n)
        - You start building a dict of the stuff you have seen, and updating the curr and max_len
        - If you see something that is part of the current substring (is in the dict and index more than l)
            - update the idx of that character in the dict to the new value
            - update the substring to be 1 to the right of the og character that is now repeating (1 + old_idx, where s[old_idx]==s[r])
            - since the substring is not built explicitly, we just update the currentlength
            - shift the left ptr
        """
        s_len=len(s)
        if s_len<2:
            return s_len

        seen_dict={}
        l,r=0,1
        max_len=1
        curr_len=1
        seen_dict[s[0]]=0

        while r<s_len and l<=r: 
            if s[r] in seen_dict and seen_dict.get(s[r])>=l: #if the repeating character is part of the current substr
                curr_len=r-seen_dict.get(s[r]) #update curr_len (substring now implicitly starting 1+old_idx)
                l=seen_dict.get(s[r])+1 # update l to one right of old_idx
                seen_dict[s[r]]=r # updates seen_dict
                r+=1 #shift r right
                
            else:
                seen_dict[s[r]]=r #add (or update) to dict
                curr_len+=1 #increment curr_len
                if curr_len>max_len: #update max_len if need be
                    max_len=curr_len 
                r+=1 #shift r right once
        
        return max_len
        
        
