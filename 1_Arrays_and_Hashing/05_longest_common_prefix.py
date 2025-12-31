class TrieNode:
    def __init__(self, val=False):
        self.val=val
        self.children={}
class Solution:
    """
    Problem: 14. Longest Common Prefix
    https://leetcode.com/problems/longest-common-prefix/description/

    n=length of shortest string, m=number of strings, S=total number of characters across all strings
    
    Horizontal Scan:
    - Time= O(n*m) , Space=O(1)

    Trie:
    - Time = O(S) to build trie + O(n) to extract prefix -> O(S), S~mL(where L is averge length of strings)
    - mL is comparable of nm, but also uses extra space O(S). That is why horizontal scan is faster
    
    """
    def __init__(self):
        self.root=None
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time=O(n*m) -> n is the length of the shortest string and m is num stirngs
        Space=O(n) -> can be O(1) if you do vertical scannign
        """
        # return self.horizontalScan(strs)
        root=TrieNode()
        for s in strs:
            if not s:
                return ""
            self.insertIntoTrieNode(root,s)
        return self.findLongestPrefix(root)
        
    def findLongestPrefix(self,root):
        res=""
        temp=root
        while len(temp.children)==1 and not temp.val:
            for k,v in temp.children.items():
                res+=k
                temp=v
        return res 
    
    def insertIntoTrieNode(self, root, s):
        temp=root
        for c in s:
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
        temp.val=True
    
    def horizontalScan(self, strs):
        prefix=strs[0]
        n=len(strs)

        for i in range(1,n):
            minLen=min(len(strs[i]),len(prefix))
            j=0
            while j<minLen and strs[i][j]==prefix[j]:
                j+=1
            prefix=prefix[:j]
        return prefix
            


        