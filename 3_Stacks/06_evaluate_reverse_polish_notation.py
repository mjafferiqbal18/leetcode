class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Problem: 150. Evaluate Reverse Polish Notation
        https://leetcode.com/problems/evaluate-reverse-polish-notation/

        Intuition:
        - Just store numbers in the stack
        - Whenever you get operations, you pop from stack to perform them, and then push accordingly
        - This is assuming that the operations and tokens will be in the correct order

        NOTE: you need to be mindful of truncation towards zero:
            - // in python rounds down (so if pos, truncates to 0, but if neg, then rounds down in practice)
            - best way is to do the division and then cast to int() which will truncate towards 0 in both positive and negative cases
        
        Time:
        - O(n)

        Space:
        - O(n)
        """
        stack=[]
        for c in tokens:
            if c=="+":
                stack.append(stack.pop()+stack.pop())
            elif c=="-":
                b,a=stack.pop(),stack.pop()
                stack.append(a-b)
            elif c=="*":
                stack.append(stack.pop()*stack.pop())
            elif c=="/":
                b,a=stack.pop(),stack.pop()
                stack.append(int(a/b)) #truncates towards 0 (int(-7/3)=int(-2.33)=-2; // floors towards negative infinity i.e -7//3=-2.33=-3)
            else:
                stack.append(int(c))

        return stack[0]

