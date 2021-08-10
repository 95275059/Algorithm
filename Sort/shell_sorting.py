def shell_sorting(alist):
    # 希尔排序是对插入排序的优化
    # 希尔排序又叫缩小增量排序
    # 时间复杂度：平均：o(n**1.3), 最多：o(n**2)，最少：o(n),
    # 空间复杂度：o(1)
    # 稳定性：不稳定
    length = len(alist)
    gap = length // 2
    while gap > 0:
        for i in range(gap):
            gap_insert_sort(alist, i, gap)
        gap = gap // 2


def gap_insert_sort(alist, start_index, gap):
    length = len(alist)
    for i in range(start_index+gap, length, gap):
        currnode = alist[i]
        position = i
        while position > start_index and alist[position-gap] > currnode:
            alist[position] = alist[position-gap]
            position -= gap
        alist[position] = currnode