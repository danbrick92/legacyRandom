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

def random_select(unsorted,i,l=0,r=-1):
    # Select r if not provided
    if r == -1:
        r = len(unsorted)
    l_unsorted = len(unsorted[l:r])
    if l_unsorted > 1:
        # Choose pivot, swap if not 0 index
        p = random.randint(l, r-1)
        if p > l:
            p_val = unsorted[p]
            unsorted[p] = unsorted[l]
            unsorted[l] = p_val
        # Partition arrays
        unsorted, j = partition(unsorted,l,r)
        # Condition
        if i == j:
            return unsorted[j]
        elif i < j:
            return random_select(unsorted, i, l, j)
        elif i > j:
            return random_select(unsorted, i, j+1, r)
    else:
        return unsorted[i]

if __name__ == "__main__":
    i = 6
    x = random_select([1,2,3,4,5,6,7,8],i)
    print("Smallest entry #{}: {}".format(i+1,x))