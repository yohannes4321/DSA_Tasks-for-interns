"""what i read about HeapSort

time complexity is O(nlogn)
it use heap data structure and inplace

steps 
    1,Build heap sort which is heapifying  Array calling 
    Commonly max heapify on the root node from the last None Leaf node
    2. bY Swapping the first root index with the last element delete the last element
    which means decrease the size of Array by one and heapify the array once again
    and 
     
First convert the array into a max heap using heapify,this  is  in-place. The array elements are re-arranged to follow heap properties.
 Then one by one delete the root node of the Max-heap and replace it with the last node and heapify. Repeat this process while size of heap is greater than 1.

Rearrange array elements so that they form a Max Heap.
Repeat the following steps until the heap contains only one element:
Swap the root element of the heap (which is the largest element in current heap) with the last element of the heap.
Remove the last element of the heap (which is now in the correct position). We mainly reduce heap size and do not remove element from the actual array.
Heapify the remaining elements of the heap.
Finally we get sorted array.

Step 1: Treat the Array as a Complete Binary Tree
 
Step 2: Build a Max Heap

Step 3: Sort the array by placing largest element at end of unsorted array.

"""