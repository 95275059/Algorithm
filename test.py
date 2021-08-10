def shell_sorting(alist):
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap):
            insert_sorting_gap(alist, i, gap)
        gap = gap // 2

def insert_sorting_gap(alist, start_index, gap):
    for i in range(start_index+gap, len(alist), gap):
        curnode = alist[i]
        position = i
        while position > start_index and alist[position-gap] > curnode:
            alist[position] = alist[position-gap]
            position -= gap
        alist[position] = curnode