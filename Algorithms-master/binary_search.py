def binary_search(sorted,search):
    l = len(sorted)
    if l == 0:
        m = -1
    elif l == 1:
        if sorted[0] == search:
            m = 0
        else:
            raise Exception("Index not found")
    else:
        split = l//2
        if sorted[split] == search:
            m = split
        elif search < sorted[split]:
            m = binary_search(sorted[:split],search)
        else:
            m = binary_search(sorted[split:],search)
            m+=len(sorted[:split])
    return m

if __name__ == "__main__":
    sorted_array = [1,2,3,4,5,6,7,8,11]
    m = binary_search(sorted_array,11)
    print(m)