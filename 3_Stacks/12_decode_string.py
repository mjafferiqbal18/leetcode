class Solution:
    def decodeString(self, s: str) -> str:
        """
        Problem: 394. Decode String
        https://leetcode.com/problems/decode-string/

        Intuition:
        - If it was linear, it could be very simple, however, the trick to this is that the encoding can be nested
        - Since itll be nested, then we need to unravel(by multiplying by k)/resolve the most recent case
        - And since we need to unravel/resolve the most recent case, we should use a stack
        - Now we can handle nesting in the following ways:
            - keep adding chars from the string onto the stack
            - the moment we come across a ']', we building the string up till '[', get the number and multiply it
            - once resolved, add the string back onto the stack 
        - finally join the stack and return

        Time:
        - O(n)

        Space:
        - O(n)


        
        """

        stack=[]
        i=0
        n=len(s)

        while i<n:
            if s[i]==']':
                strToRepeat=[]
                #build the string until [
                while stack and stack[-1]!='[':
                    strToRepeat.append(stack.pop())
                #pop the [
                stack.pop()
                #reverse the string (since we've been popping) 
                strToRepeat="".join(reversed(strToRepeat))
    
                num=""
                #build the number
                while stack and stack[-1].isnumeric():
                    num+=stack.pop()
                #reverse it until its reverse
                num=num[::-1]
                #store the result onto the stack
                stack.append(strToRepeat*int(num))
            else:
                stack.append(s[i])
            i+=1
            # print(stack)
        return "".join(stack)