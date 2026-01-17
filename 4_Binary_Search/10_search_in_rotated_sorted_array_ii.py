class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Problem: 81. Search in Rotated Sorted Array II
        https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

        Intuition:
        - Similar to search in rotated sorted array 1 (first coded it up)
        - Now mid can be equal to st and also end
            - If mid==st==end:
                - How to make the decision: 
                    - we can trim the search space by bringing in l and r pointers and continue
                    - or we can check (via iteration) which half has only one element (one end will)
            - Else:
                - st==mid, mid!=end:
                    - this means that st to mid we have the same element
                    - [22223456] or [2245222]
                - st!=mid, mid==end:
                    - this means that mid to end we have the same element (we can prune that side since we compare target to mid first)
                    - [22223456] -> [34562222]
                - st,mid,end are all different:
                    - we can use the regular rotated sorted array 1 logic to prune a side


        """
        st=0
        end=len(nums)-1

        while st<=end:
            mid=(st+end)//2

            if target==nums[mid]:
                return True
            
            if nums[st]==nums[mid]==nums[end]:
                #do something
                st=st+1
                end=end-1
            elif nums[st]==nums[mid]: #st -> mid is the same number, which is not our target
                st=mid+1
            elif nums[mid]==nums[end]: #mid -> end is the same number, which is not our target
                end=mid-1
            else: #st, mid, end are different numbers
                if nums[st]<=nums[mid]: #left half is sorted, st could be equal to mid
                    if target>=nums[st] and target<nums[mid]: #go left
                        end=mid-1
                    else:
                        st=mid+1
                else: #right half is sorted
                    if target>nums[mid] and target<=nums[end]:
                        st=mid+1
                    else:
                        end=mid-1
        return False
                    

        
        """
        target=4 | 5
        2222224
        2222242

        2222242 

        2242222

        2222245
        2245222

        mid==end# you can prune right side
        """
        n=len(nums)
        st=0
        end=n-1
        
        while st<=end:
            mid=(st+end)//2
            if nums[mid]==target:
                return True

            if nums[mid]==nums[end]==nums[st]: #all same, bad scene
                if len(set(nums[st:mid]))>1: #non distinct elements
                    end=mid-1 #go left
                else:
                    st=mid+1
            elif nums[mid]==nums[end]: #mid to end is the same number
                end=mid-1 #go left
            elif nums[mid]==nums[st]: #st to end is the same number
                st=mid+1 #go right
            elif nums[st]<nums[mid]: #left half is sorted
                if target>=nums[st] and target<nums[mid]: #go left
                    end=mid-1
                else:
                    st=mid+1
            else:
                if target>nums[mid] and target<=nums[end]: #go right
                    st=mid+1
                else:
                    end=mid-1
        return False


        