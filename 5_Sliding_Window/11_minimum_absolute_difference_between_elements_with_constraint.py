class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        """
        First, sort nums increasing. Then we can make one pass through, and note that this tells us that the current value will always be greater than every value we have seen before. 
        So we use two heaps, one to check whether there is a possible difference candidate to the left of the current value, and one to tell us whether there is a candidate to the right. 
        Each heap will contain (index, value) pairs (index here referring to original unsorted index); the left heap is a min heap since we look for the smallest indices first on the left, and the right heap is a max heap since we look for the largest indices first on the right (to guarantee we're far enough away). 
        Then as we make our one pass, we check whether the top element of either heap is far enough away, and if it is, we pop it and consider it as a candidate for minimum difference. We're okay to pop them off, since we know we're looking at elements in ascending order, so we know we are already considering the closest possible match for that number.

        IMPORTANT:
        - When you are at (val, index), every element you’ve seen so far has value ≤ val. 
        - The first time an earlier element becomes “eligible” by index distance, it gives the smallest possible value difference it will ever have with any later element 
        - Any later elem will be greater than curr and thus have a greater abs difference, so prev can be safely discarded

        - The left heap (is minheap) so elem farthest left (and smaller than us, since we are going in sorted order)
        - The right heap (is maxheap) so elem farthest right (and smaller than us, since we are going in sorted order)
        

        Time complexity: O(nlogn) -- we sort length-n array, and then do 2n logn inserts into heap
        Space complexity: O(n)


        """
        sortedNums = sorted((nums[i], i) for i in range(len(nums)))
        heapLeft, heapRight = [], []
        minDiff = float('inf')

        for i in range(len(sortedNums)):
            val, index = sortedNums[i] 
            heapq.heappush(heapLeft, (index, val)) # min heap. smallest indices pop off (look for match on left side)
            heapq.heappush(heapRight, (-index, val)) # max heap. biggest indices pop off (look for match on right side)

            # because of sorting, everything in either heap is already less than val. so we just need to do an index check
            while heapLeft and heapLeft[0][0] + x <= index:# heapLeft we use to check whether current number can be the front half
                minDiff = min(minDiff, val - heapq.heappop(heapLeft)[1])
            while heapRight and heapRight[0][0] + x <= -index: # heapRight we use to check whether current number can be back half 
                minDiff = min(minDiff, val - heapq.heappop(heapRight)[1])
            # note that we don't mind popping these off, because we are always checking their distance with the closest valid partner
        return minDiff
        
        """
        ussing sortedlist with bisect_left
        """
        from sortedcontainers import SortedList

        if x == 0:
            return 0

        arr, best_dist = SortedList([]), float('inf')
        for i in range(x, len(nums)):
            arr.add(nums[i - x])
            v = nums[i]

            pos = arr.bisect_left(v)
            if pos < len(arr):
                best_dist = min(best_dist, abs(arr[pos] - v))
            if pos > 0:
                best_dist = min(best_dist, abs(arr[pos - 1] - v))
        
        return best_dist


        """
        n^2 solution
        """

        n=len(nums)
        res=float('inf')

        for i in range(n):
            for j in range(i+x,n):
                res= min(res,abs(nums[j]-nums[i]))
        return res


        