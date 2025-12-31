class Solution:
    """
    Problem: . Encode and Decode Strings
    https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode250

    Intuition:
    - How would you blindly know where a string starts and where a string ends? You would need to know the length of the string (i.e. where it starts and where it ends)
    - To encode, you can put length of string at start (so you know how big the string is)
    - but then you also need to know how long the number is that encodes the length, and where the string starts, so you put a 'marker' after the length
    - this allows you to decode easily by reading in the number until the marker, then grabbing the string of that length, and repeating

    ["n#eet","code","love","you"]
    "5#n#eetcode love you" -> after encoding, str will start with a number followed by a #
    So this way even if # appears again, we know that we dont need to break string there
    
    """

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            len_s= len(s)
            res+= str(len_s)+"$"+s
        return res

    def decode(self, s: str) -> List[str]:
        """
        The string will always start with a num and then a #
        We break the string there, and then the remaining string will have a number and # again
        """

        res=[]
        i=0
        len_s=len(s) 
        while i<len_s:
            j=i
            while s[j]!="$":
                j+=1
            length= int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
    
    


