class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Problem: 229. Majority Element II
        https://leetcode.com/problems/majority-element-ii/

        Inutition:
        - Use hashmap to count occurence: O(n) time and O(n) space
        - If we look at the output of examples, we realize that at max 2 elements can have count>floor(n/3) -> intuitively that makes sense
        - We need to find a way to do this in O(2) space
            - We can keep a hashmap, and the moment its length>2, we need to evict something
            - the moment length>2, we decrement element counts, and evict the keys for which count is now 0 (garunteed that we would evict atleast one element)
            - The last elements to survive are the best candidates:
                - we check their counts in 2 passes. if they have count>floor(n/3) then its all good
                - if not, then theres no element in the array with count>floor(n/3)
            - Watch NEETCODE video for best visualization! https://www.youtube.com/watch?v=Eua-UrQ_ANo&t=317s

        O(n) time, O(1) space
        assume n=8, 8//3-> 2, an element needs to appear more than 2, so needs to have count atleast 3
        8//3 -> 2 -> only 2 elements can have count > floor(n/3)

        we only need to keep record for 2 elements -> space=O(2) = O(1)
        we add elems to hashmap, if more than 2 elems, we will decrement all elem count, remove if ==0
        at the end, you check remaining elems in hashmap, get their count from array and confirm if >2
        because if all elems are unique, at the end 2 elems will survive that have only one count
        """
        runningMap={}
        for n in nums:
            if n not in runningMap:
                runningMap[n]=0
            runningMap[n]+=1

            #check map lenght
            if len(runningMap)>2:
                new_count = defaultdict(int)
                for num,c in runningMap.items():
                    if c > 1:
                        new_count[num]=c - 1
                runningMap = new_count
        
        res=[]
        for num in runningMap:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res

        """
        O(n) space and time
        """
        n=len(nums)
        target=n//3
        count={}
        for num in nums:
            if num not in count:
                count[num]=0
            count[num]+=1
        
        res=[]
        for k,v in count.items():
            if v>target:
                res.append(k)
        return res
        