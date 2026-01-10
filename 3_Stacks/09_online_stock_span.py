class StockSpanner:
    """
    Problem: 901. Online Stock Span
    https://leetcode.com/problems/online-stock-span/

    Inuition:
    - Brute force would be O(n^2) where for each element you would traverse backwards
    - Want a way to do it in linear time -> you have to store/ carry something forward to enable that
    - at idx=i, you want to know the previous idx=j such that all elements between i and j are <= elem[i]
        - if idx=i+1 <= i, then the span[i+1]= span[i]+1
        - if idx=i+1 > i, then span[i+1]=1, and anything less elem[idx] will have its span blocked from being extended

        - We could use a monotonically decreasing stack:
            - if stack[-1] <= curr -> curr can absorb span of whatevers on the stack
            - if sta(ck[-1] > curr -> curr cant absorb span and is added to the stack
            - similar to the daily temperatures question, where you can carry forward monotonic information to be resolved accordingly by the next element
        - Example: [7,2,1,2] ; tuple elements are (price,span)
                    (7,1) -> because stack before it is empty
                    (7,1), (2,1) -> elem on top of stack is greater (7>2) so cant absorb its span
                    (7,1), (2,1), (1,1) ->  elem on top of stack is greater  (2>1) so cant absorb its span
                    (7,1), (2,3) -> becase curr=2 can absorb span of (1,1) and (2,1) since it is >= them
                        - a new curr >= 2 can then absorb (2,3)
                        - a new curr < 2 cant absorb (2,3) and will be placed on the stack to absorb
        - Example2: [7,34,1,2]
                    (7,1)
                    (34,2)
                    (34,2),(1,1)
                    (34,2),(2,2)

    Time:
    - O(n)

    Space:
    - O(n)

    use a monotonically decreasing stack
    """

    def __init__(self):
        self.stack=[] #pair= price,span     

    def next(self, price: int) -> int: 
        span=1 #default span
        while self.stack and self.stack[-1][0] <= price: #if whatevers on top is <= to you
            span += self.stack[-1][1] #absorb span of whatevers smaller or equal to you
            self.stack.pop() #remove that element from the stack
        self.stack.append((price, span)) #append your (price,span) for the next element
        return span

    

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)