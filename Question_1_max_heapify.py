def max_heapify(Array, current_index):
    largest = current_index  # initialize the largest with current index
    while True:
        left = 2 * current_index + 1  # this is the left child index
        right = 2 * current_index + 2  # this is the right child index
        if left < len(Array) and Array[left] > Array[largest]:
            # to cheak if the left index is less than the size of Array so it will stop at the end of the leaf index
            # the value of the left child is greater than the value of the largest index 
            # we gona assign the largest with left index
            largest = left
        if right < len(Array) and Array[right] > Array[largest]:
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