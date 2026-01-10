class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Problem: 71. Simplify Path
        https://leetcode.com/problems/simplify-path/

        Intuition:
        - First, we need to remove the '/' -> we can split the string on '/' (removes all '/' and breaks the string accordingly) and add those later when building our final path
        - Since we will need to undo/remove most recent parts of the path (for example when we see '..' ) -> we should use a stack
        - Once path is split, we can process 
            - stack will represent the path, needs to start with '/'
            - if elem=='' then add '/' to stack UNLESS stack top already has a '/'
            - if elem=='.' then dont add anything to the stack
            - if elem=='..' then pop last two elems if len(stack>=2) (last will be '/' and secondlast will be elem to remove)
            - otherwise just add to stack, and then also add a '/'

        Time:
        - O(n)

        Space:
        - O(n)
        """

        splitPath=path.split('/') #should hold either /, ., .., words
        stack=['/']
        i=0
        n=len(splitPath)
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

        
                    