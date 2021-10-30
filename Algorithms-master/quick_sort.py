import random

def partition(array,l,r):
    p = array[l]
    i = l+1
    for j in range(l+1,r):
        # If should be on left, swap with current and increase i
        if array[j] < p:
            ai = array[i]
            array[i] = array[j]
            array[j] = ai
            i+=1
    # Swap pivot to correct place
    al = array[l]
    array[l] = array[i-1]
    array[i-1] = al
    return array, i-1

def quick_sort(unsorted,l=0,r=-1):
    # Select r if not provided
    if r == -1:
        r = len(unsorted)
    if len(unsorted[l:r]) > 1:
        # Choose pivot, swap if not 0 index
        p = random.randint(l, r-1)
        if p > l:
            p_val = unsorted[p]
            unsorted[p] = unsorted[l]
            unsorted[l] = p_val
        # Partition arrays
        unsorted, p_ind = partition(unsorted,l,r)
        # Sort
        unsorted = quick_sort(unsorted,l,p_ind)
        unsorted = quick_sort(unsorted,p_ind+1,r)
        return unsorted
    else:
        sorted = unsorted
    return sorted

if __name__ == "__main__":
    x = quick_sort([3,1,2,4,8,7,6,9,10,13,14,15,12,18])
    print(x)