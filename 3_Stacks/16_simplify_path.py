class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Problem: 71. Simplify Path
        https://leetcode.com/problems/simplify-path/

        Intuition:
        - Since we need to undo stuff where we come across '..', we should use a stack
        
        Time:
        - O(n)

        Space:
        - O(n)
        
        """
        splitPath=path.split('/') #should hold either /, ., .., words
        stack=['/']
        i=0
        n=len(splitPath)
        # print(splitPath)
        while i<n:
            if splitPath[i]=='':
                if not (stack and stack[-1]=='/'):
                    stack.append('/')
            elif splitPath[i]=='.' and stack:
                pass
            elif splitPath[i]=='..': #what if stack empty
                if len(stack)>2:
                    stack.pop() #pop /
                    stack.pop() #pop prev dir 
            else:
                stack.append(splitPath[i])
                stack.append('/')
            i+=1
        if len(stack)>1 and stack[-1]=='/':
            stack.pop()
        return "".join(stack)

        
                    