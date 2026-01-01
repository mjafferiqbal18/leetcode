class Solution:
    """
    Problem: 344. Reverse String
    https://leetcode.com/problems/reverse-string/

    Intuition:
    - Start with 'abc' -> to reverse we swap the first and last characters with each other
    - This hints at a two pointer solution, where l=0,r=n-1 and we break when l==r (because it'll be the center element), or if odd length, the l and r will cross
        - So while condition should be l<r

    Time:
    - O(n)

    Space:
    - O(1)
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        while l<r:
            #swap logic
            temp=s[l]
            s[l]=s[r]
            s[r]=temp

            l+=1 #shifting ptrs inwards
            r-=1
            
        
        