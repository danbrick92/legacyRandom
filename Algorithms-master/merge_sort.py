def sort(a,b):
    c = []
    n = len(a) + len(b)
    i = j = 0
    for k in range(n):
        if i >= len(a):
            c.append(b[j])
            j += 1
        elif j >= len(b):
            c.append(a[i])
            i += 1
        elif a[i] < b[j]:
            c.append(a[i])
            i+=1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
    return c

def merge_sort(unsorted):
    l = len(unsorted)
    if l > 1:
        a = unsorted[:l//2]
        b = unsorted[l//2:]
        a = merge_sort(a)
        b = merge_sort(b)
        sorted = sort(a,b)
    else:
        sorted = unsorted
    return sorted

if __name__ == "__main__":
    x = merge_sort([5,4,1,8,7,2,6,3,9,10,15,13,14,12,11])
    print(x)