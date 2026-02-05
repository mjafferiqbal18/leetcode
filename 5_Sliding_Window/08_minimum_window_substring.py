from collections import deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Problem: 76. Minimum Window Substring
        https://leetcode.com/problems/minimum-window-substring/

        Intuition:
        - Lets try an O(m+n) solution
        We have countS and countT maps, we should not compare whole maps
            instead use a counter to keep track of numUniqueElems we have; you increment if countS[elem]==countT[elem], if numUniqueElems==len(countT), this is a potential solution
            Once a potential solution is found, you keep incrementing left ptr until numUniqueElems!=len(countT)
            you increment r when havecount is not equal, and you increment l when havecount is equal
            Very sliding window-y solution
        
        Watch neetcode video
        """
        if t=="":
            return ""
        countT,window={},{}
        for c in t:
            countT[c]=1+ countT.get(c,0)

        #have basically counts the first time a character's count in window == that character count in t
        have,need=0,len(countT)
        res= [-1,-1] #default vals for l,r ptrs
        resLen= float('inf')
        l=0
        for r in range(len(s)): #keeps track of right bound
            c=s[r]
            window[c]=1+window.get(c,0)

            if c in countT and window[c]==countT[c]:
                have+=1
            
            while have==need: #now you can start decreasing the window size until window becomes invalid (common pattern)
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=(r-l+1)
                window[s[l]]-=1
                #if by removing this character we made the have count less than what it needs to be
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float('inf') else ""

        """
        Brute Force
        O(n^2), we create a window at each char in S, and increase it until our hashmaps arent equal or we go out of bounds
        """
        m=len(s)
        n=len(t)  
        if n>m:
            return ""
        
        countT={}
        for character in t:
            if character in countT:
                countT[character]+=1
            else:
                countT[character]=1

        minLen=float('inf')
        minS=""
        for i in range(m):
            j=i
            countS={}
            while j<=m:
                if countS==countT:
                    if (j-i+1)<minLen:
                        minLen=j-i+1
                        minS=s[i:j]
                    break
                elif j<m:
                    if s[j] in countS:
                        if countS[s[j]]<countT[s[j]]:
                            countS[s[j]]+=1
                    elif s[j] in countT:
                        countS[s[j]]=1
                j+=1
            # print(i,j,countS,countT)
        return minS

class Solution1:
    """
    Another brute force-y solution where you compare whole maps, it should still be O(m+n) since maps are of size 26 (constant)
    
    """
    def minWindow(self, s: str, t: str) -> str:
        lenS = len(s)
        lenT = len(t)

        if lenT>lenS:
            return ""

        windowS = {}
        windowT = {}
        for c in t:
            if c not in windowT:
                windowT[c]=0
            windowT[c]+=1
        
        l = 0
        res = float('inf')
        resStr = ""
        for r in range(lenS):
            if s[r] not in windowS:
                windowS[s[r]]=0
            windowS[s[r]]+=1

            while self.isEveryCharOfTinS(windowS,windowT):
                winSize = r-l+1
                if winSize < res:
                    res = winSize
                    resStr = s[l:r+1]
                windowS[s[l]]-=1
                l+=1

        return resStr
    
    def isEveryCharOfTinS(self,windowS,windowT):
        """
        All keys of windowT must be in windowS, and windowS[k]>= windowT[k]
        """
        for k,v in windowT.items():
            if k not in windowS:
                return False
            elif k in windowS and windowS[k]< v:
                return False
        
        return True

        