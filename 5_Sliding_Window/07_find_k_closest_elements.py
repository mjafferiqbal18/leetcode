class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Problem: 658. Find K Closest Elements
        https://leetcode.com/problems/find-k-closest-elements/

        Intuition:
        - Since we want to find x (or the closed elem to x), we can do a binary search to do that
            - Remember, if we dont find x, l == r, where arr[l] is the first elem>x
        - Once we do that, we can expand window (starting size 0) between l-1 and l (l=l-1, r=l these dont include the window -> i.e. they are exclusive)
         
        First, do a binary search to find the closest element to x (can be x or something else)
        """
        n=len(arr)
        res=[]
        l,r=0,n-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]<x:
                l=mid+1
            else: #arr[mid]>=x
                r=mid 
        #l becomes closest num either x to x or the next greater and l==r
        l,r=l-1,l #either one of them could be closer to x
        
        #invariant: window = is BETWEEN l and r (so empty to start) arr[l+1:r]
        while r-l-1<k:
            if l<0: #index out of range, just increase r
                r+=1
            elif r>=n: #index out of range, just increase l
                l-=1
            elif abs(arr[l]-x)<=abs(arr[r]-x): #both are in range, compare and increase the one required
                l-=1
            else: 
                r+=1
        return arr[l+1:r] #the window starts at l+1 and ends at r-1

        
        """
        A more brute force approach where you just push to heap and then pop k times and return sorted result
        
        Time:
        - O(nlogn)

        Space:
        - O(n)
        """

        n = len(arr)
        minHeap = []

        for i in range(n):
            heapq.heappush(minHeap, (abs(x-arr[i]),arr[i]))
        
        res = []
        for i in range(k):
            diff, val = heapq.heappop(minHeap)
            res.append(val)
        
        return sorted(res)
