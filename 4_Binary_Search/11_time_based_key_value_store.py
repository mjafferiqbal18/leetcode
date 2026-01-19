class TimeMap:
    """
    Problem: 981. Time Based Key-Value Store
    https://leetcode.com/problems/time-based-key-value-store/

    Intuition:
    - We can see that timestamps for a key will be increasing monotonically -> we can do a regular binary search on them
        - if timestamp[mid]==timestamp -> value[mid] is the best one
        - if timestamp[mid]>timestamp -> value[mid] is unusable -> decrease upperbound
        - if timestamp[mid]<timestamp -> store value[mid] so far and increase lower bound
    
    Time:
    - O(logn)

    Space:
    - O(n)
    
    """

    def __init__(self):
        self.map={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value,timestamp))
        else:
            self.map[key]=[(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        res=""
        if self.map.get(key)!=None: # do a binary search
            values=self.map.get(key)
            st=0
            end=len(values)-1

            while st<=end:
                mid= (st+end)//2
                if values[mid][1]==timestamp:
                    return values[mid][0]
                
                if values[mid][1] < timestamp:
                    res=values[mid][0]
                    st=mid+1
                else: #values[mid][1] > timestamp   
                    end=mid-1
        return res

    def get2(self, key: str, timestamp: int) -> str:
        res=""
        if self.map.get(key)!=None: # do a binary search
            values=self.map.get(key)
            st=0
            end=len(values)-1
            while st<=end:
                mid=(st+end)//2
                if timestamp==values[mid][1]: #we are at upperbound of timestamp
                    return values[mid][0]
                elif timestamp>values[mid][1]:
                    # res=values[mid][0] -> you can store the best one so far, and continue the binary search 
                    # st=mid+1 -> these two lines of code are enough
                    if mid+1<=end and values[mid+1][1]>timestamp: #look ahead
                        return values[mid][0] #if the next t > timestamp
                    elif st==end:
                        return values[mid][0]
                    else: #go right
                        st=mid+1
                elif timestamp<values[mid][1]: #go left
                    end=mid-1
        return res
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)