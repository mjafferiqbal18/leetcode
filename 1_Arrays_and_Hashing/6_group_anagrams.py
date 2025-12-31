class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Problem: 49. Group Anagrams
        https://leetcode.com/problems/group-anagrams/description/

        Intuition:
        - Two strings are anagrams if they have the same character count
        - We build character count for each string, and hash them to group them together, storing the strings in a list as the value
        - Two options to build character count: 
            - (i) use a dict (which will have to be sorted because dict keys are not ordered, and converted to a tuple in order to be hashed)
            - (ii) recognize that characters are bounded (26), so we can use an array to store the counts, and then convert to tuple to hash
        
        Time Complexity:
        - n=number of strings, m=length of longest string (we are talking about worst case here)
        - n*m to build counts, since we are going over m characters for all n strings = O(nm)

        Space Complexity:
        - n=number of strings
        - n*26 to store counts = O(26n) = O(n)
        """
        strsLen=len(strs)
        if strsLen==1: #if there's only one string
            return [strs]
        
        res=defaultdict(list) #each key will have a default empty list as value
        
        for s in strs:
            count=[0]*26 
            for c in s:
                count[ord(c)-ord('a')]+=1 #use ord to index into the array
            res[tuple(count)].append(s) #convert counts to tuple, hash to index into dict, and store the string as value
        
        return [res[k] for k in res]


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """
        ["eat","tea","tan","ate","nat","bat"] -> [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        Time: O(numStrings * avgStringLength * 26(log(26)))
        """
        if len(strs)<=1:
            return [strs]
        tupDict={}
        for s in strs:
            tup=self.formTuple(s)
            if tupDict.get(tup) is not None:
                tupDict[tup].append(s)
            else:
                tupDict[tup]=[s]
        res=[]
        for tup,groupedStrings in tupDict.items():
            res.append(groupedStrings)
        return res

    def formTuple(self,s:str)-> tuple:
        characters={}
        for character in s:
            if characters.get(character):
                characters[character]+=1
            else:
                characters[character]=1
        return tuple(sorted(characters.items()))