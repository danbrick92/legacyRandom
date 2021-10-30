def sort(a,b):
    c = []
    splits = 0
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
            splits += (len(a[i:]))
    return c, splits

def merge_and_count_inv(unsorted):
    l = len(unsorted)
    if l > 1:
        a = unsorted[:l//2]
        b = unsorted[l//2:]
        a, s1 = merge_and_count_inv(a)
        b, s2 = merge_and_count_inv(b)
        sorted, s3 = sort(a,b)
        splits = s1 + s2 + s3
    else:
        sorted = unsorted
        splits = 0
    return sorted, splits

if __name__ == "__main__":
    x, splits = merge_and_count_inv([1,5,3,2,6,4])
    print("Splits: {}, Sorted {}".format(splits,x))