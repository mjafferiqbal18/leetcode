class Solution:
    """
    Problem: 912. Sort an Array
    https://leetcode.com/problems/sort-an-array/description/

    Just need to know how to implement some sorting algos, if they are in place [O(1) space], and what their time complexities are
    
    - MergeSort:
        - Divide until single elements, then merge
        - Time: O(nlogn)
        - Space: O(1) or O(nlogn)

    - HeapSort:
        - Build a heap, pop from it n times
        - Time: O(nlogn)
        - Space: O(1) since you heapify

    - QuickSort:
        - Pick a pivot, use L,R ptrs to ensure everything to l is smaller and everything to r is smaller
        - Time: Best O(nlogn), Avg O(nlogn), Worst (n^2)
        - Space: O(1)
        - You need to pick a pivot that is close to median

    - InsertionSort:
        - Insert each element into its correct position in a growing sorted prefix
        - Time: Best O(n) [nearly sorted], Avg = O(n^2), Worst = O(n^2)

    - SelectionSort:
        - Repeatedly select minimum and place it at the front
        - Time = O(n^2) (best/avg/worst)
        - Space= O(1)

    - BubbleSort:
        - Bubble (swap adjacent out of place elements) -> call bubble n times 
        - Time = O(n^2) (best/avg/worst)
        - Space = O(1)
    
    - Non-comparion sorting:
        - Counting Sort
        - Radix Sort
        - Bucker Sort 
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        MergeSort:
            - Recurse until size == 1 (l>=r)
            - Merge step (similar to merging two linked lists)
        """
        def merge(arr, L, M, R):
            left,right= arr[L:M+1], arr[M+1:R+1] #creating temporary array
            i, j, k = L, 0, 0 #j,k are going to be at the beginning of the subarrays left and right

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            #ensure remaining array is added
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l>=r: #if size of the array is 1, l==r
                return
            m=(l+r) // 2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,m,r)

        mergeSort(nums,0,len(nums)-1)
        return nums
        