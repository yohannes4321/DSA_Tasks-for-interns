def max_heapify(Array, current_index,heap_size):
    largest = current_index  # initialize the largest with current index
    while True:
        left = 2 * current_index + 1  # this is the left child index
        right = 2 * current_index + 2  # this is the right child index
        if left < heap_size and Array[left] > Array[largest]:
            # to cheak if the left index is less than the size of Array so it will stop at the end of the leaf index
            # the value of the left child is greater than the value of the largest index 
            # we gona assign the largest with left index
            largest = left
        if right < heap_size and Array[right] > Array[largest]:
            # check if the right index is within bounds and if right child is greater than the largest
            largest = right
        if largest != current_index:
            # to cheak if the right index is less than the size of Array so it will stop at the end of the right index
            # the value of the right  child is greater than the value of the largest index 
            # we gona assign the largest with right  index

            Array[current_index], Array[largest] = Array[largest], Array[current_index]
            # move down the tree to the largest child index
            current_index = largest
        else:
            break 
            # terminate when current_index is same as largest
def heapify(Array):
    # range of Non leaf Node is from 0  to len (Array)//2 -1 
    # start from non leaf node  and come backward and appliy max-heapify function 
    for i in range(len(Array)//2 -1,-1,-1):
        max_heapify(Array,i,len(Array))
def heapSort(Array):
    heapify(Array)  # Building max heap
    # deleting element from the heap one by one
    for i in range(len(Array) - 1, 0, -1):
        # swaping the first element with the last element 
        Array[0], Array[i] = Array[i], Array[0]
        # Call max_heapify on the reduced heap
        max_heapify(Array, 0, i)
arr1 = [1, 7, 3, 2, 16]
heapSort(arr1)
print(arr1)
"""
steps 
    1,Build heap sort which is heapifying  Array calling 
    Commonly max heapify on the root node from the last None Leaf node
    2. bY Swapping the first root index with the last element delete the last element
    which means decrease the size of Array by one and heapify the array once again
     """