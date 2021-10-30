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

def get_index_tuple_list(tuple_list, index):
    retval = []
    for t in tuple_list:
        retval.append(t[index])
    return retval

def closest_pair(px,py):
    l = len(px)
    # Split arrays
    qx = px[:l//2]
    qy = py[:l//2]
    rx = px[l//2:]
    ry = py[l//2:]
    # Recurse
    p1 = closest_pair(qx, qy)
    p2 = closest_pair(rx, ry)
    # S


def closest_pairs(unsorted):
    l = len(unsorted)
    if l > 1:
        a = unsorted[:l//2]
        pairs = closest_pair
    else:
        if l == 0:
            pairs = []
        else:
            pairs = (unsorted[0],unsorted[0])
    return pairs

if __name__ == "__main__":
    pairs = closest_pairs([(1,2)])
    print("Closest Pairs: {}".format(pairs))