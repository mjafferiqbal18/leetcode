class FreqStack:
    """
    Problem: 895. Maximum Frequency Stack
    https://leetcode.com/problems/maximum-frequency-stack/

    Observations:
    - Normal stack problems only care about recency, normal heap problems only care about frequency; this problem cares about both
    - Mentally the thought should be something like a stack inside each frequency bucket
    - Then we observe that frequency only ever increases by 1, never jumps
        - this means we dont need a heap, we can do with simple bucketing / indexing by frequency
    - Finally, we need to return the most recent and most frequent:
        - so we use a stack to record elements reaching a certain frequency
        - keep track of the highest frequency to point to the stack in that bucket

    Intuition:
    - We can map a number to its count, and also map a count to the numbers against it
    - Then we see a number, we update its count, and add the number into the countToNum[count].append -> most recent element at this count
    - Also use a variable to track the highest count seen so far
    - When we pop, we go to highest count's countToNum, and pop the number
    - Once popped, we decrement that number's count as well in numToCount
    - Finally we update the variable tracking the highest count


    - We can use a heap to keep track of max frequency, elem of the heap should be ()
  
    You use a hashmap to map frequency count -> number
    Keep track of max frequency
    Also map a number -> its frequency
    When adding elems, increase its frequency, and append to the freqmap
    when popping, go to max freq, pop it (it will be the most frequent at that frequency)
    
    Time:
    - Pushing is O(1)
    - Popping is O(1) ammortized:
        - regular popping is O(1)
        - only cost is adjusting the highestCount:
            - highestCount only ever increases during push
            - During pop, it only decreases
            - Over the entire lifetime of the structure, highestCount can move down at most as many times as it moved up
            - So across all operations, the total work done by that while loop is linear in the number of pushes, making each pop amortized O(1).
    """
    def __init__(self):
        self.numToCount={} #map a number to its count
        self.highestCount=0 #points to the current highest count
        self.countToNums={} #map a count to the numbers seen -> the val is a stack

    def push(self, val: int) -> None:
        #update the count of the number
        if val not in self.numToCount: 
            self.numToCount[val]=0
        self.numToCount[val]+=1

        #Store the number against the count
        if self.numToCount[val] not in self.countToNums:
            self.countToNums[self.numToCount[val]]=[]
        self.countToNums[self.numToCount[val]].append(val)

        #update the highest count seen
        self.highestCount=max(self.highestCount,self.numToCount[val])
        
    def pop(self) -> int:
        # print(self.countToNums,self.highestCount)
    
        # pop the most recent addition against the highest count
        val=self.countToNums[self.highestCount].pop() #pop number

        # decrement the count of this number as well
        self.numToCount[val]-=1 #decrement its count

        # if the stack against the highest count is empty
        if not self.countToNums[self.highestCount]:  #if the array is empty for this frequency
            del self.countToNums[self.highestCount] #delete the pair (key,[])
            #search for the next highest count
            while self.highestCount>0 and self.highestCount not in self.countToNums:
                self.highestCount-=1
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()