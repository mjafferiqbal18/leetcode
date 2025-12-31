class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Problem: 347. Top K Frequent Elements
        https://leetcode.com/problems/top-k-frequent-elements/


        Intuition:
            Complexity should be better than nlogn -> no regular sorting
            Calculate frequency using hashmap: O(n) 
            Heapify the array: O(n) (https://www.youtube.com/watch?v=pLIajuc31qk&t=850s) <- Why heapify is O(n)
            Pop top k elements: O(klogn)
            Total time: O(n)+O(n)+O(klogn)

        OR 
            When the elements are bounded (i.e. n is small), you can do a bucketsort
            Do a bucketsort -> map counts to indicies of an array, elements will be the keys from the dict
            Is better than heapsort because:
            Filling the bucket array: O(n)
            returning answer from the bucket array: O(k)
            Total time: O(n)+O(n)+O(k)

            Why does it work? Counts are bounded by length of the original array + 1 (an element could occur a max of len(array) times)

            In practice bucketsort is slower (sigh)
        """
        # import heapq
        count={}
        for n in nums:
            count[n]= 1 + count.get(n,0)
        
        max_heap = [(-value,key) for key, value in count.items()]
        heapq.heapify(max_heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res

        #return self.bucketSortSolution(count,k,len(nums))

    def bucketSortSolution(self, count: Dict[int,int], k: int, numsLen:int) -> List[int]:
        bucket=[[] for _ in range(numsLen+1)]
        for key,v in count.items():
            bucket[v].append(key)
        # print(bucket)
        res = []
        for i in range(len(bucket)-1,0,-1): #0 is not included (len(bucket)-1) = (numsLen+1-1)=numsLen
            for bucketVal in bucket[i]:
                res.append(bucketVal)
                if len(res)==k:
                    return res


    def heapifySolution(self, count: Dict[int,int], k: int) -> List[int]:
        max_heap = [(-value,key) for key, value in count.items()]
        heapq.heapify(max_heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res


        





        