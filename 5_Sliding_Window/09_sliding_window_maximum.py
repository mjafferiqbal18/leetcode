class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Problem: 239. Sliding Window Maximum
        https://leetcode.com/problems/sliding-window-maximum/

        Intuition:
        - Brute force is O(kn) = O(n^2), we need to do better
        - We can use a fixed size sliding window, but how to store max in a linear fashion?
            - Observations: Once a new max comes in, all maxes to the left are not valid
            - We can use a monotonically decreasing queue to represent the window

        Brute force O(kn):
            slide window, take max
    
        Optimal = O(n)
        Use a monotonically decreasing queue to change your sliding window size
        """

        output=[]
        l,r=0,0
        q=collections.deque() #store indicies, because indices are unqiue (values can be same)
        n=len(nums)
        res=[]
        while l<=r and r<n:
            # print(l,r,res,q)
            while q and nums[q[-1]]<nums[r]: #ensure that the queue is monotonically decreasing (while elem is greater than queue end, pop queue)
                q.pop()
            q.append(r) #append yourself
            
            if (r-l+1)==k: #if we are at the window size
                res.append(nums[q[0]]) #the maximum for this window will always be at left most end of queue (since this is a monotonically decreasing queue)
                # since we now have to slide the window we need to evict l. l can possibly be at the left most end of the queue, so we need to handle that as well
                if l==q[0]: 
                    q.popleft()
                l+=1
            r+=1
            
        return res

        """
        Brute force O(kn)
        
        """

        while r<len(nums):
            #before appending, we need to make sure no smaller value exists in our queue
            while q and nums[q[-1]]<nums[r]: #while top value in queue < nums[i]
                q.pop()
            q.append(r)

            #if l is out of bounds (i.e. l> leftmostval in q)
            if l>q[0]:
                q.popleft()
            
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output


        