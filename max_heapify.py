def Max_heapify(Array, current_index):
    largest = current_index  # initialize the largest with current index
    while True:
        left = 2 * current_index + 1  # this is the left child index
        right = 2 * current_index + 2  # this is the right child index
        if left < len(Array) and Array[left] > Array[largest]:
            # check if the left index is within bounds and if left child is greater than the largest
            largest = left
        if right < len(Array) and Array[right] > Array[largest]:
            # check if the right index is within bounds and if right child is greater than the largest
            largest = right
        if largest != current_index:
            # swap the current index with the largest child
            Array[current_index], Array[largest] = Array[largest], Array[current_index]
            # move down the tree to the largest child index
            current_index = largest
        else:
            break  # terminate when current_index is the same as largest
