def select_sorting(alist):
    # 时间复杂度：o(n**2)
    # 空间复杂度：o(1)
    # 稳定性：不稳定
    length = len(alist)
    for i in range(length-1, 0, -1):
        max_index = i
        for j in range(0, i):
            if alist[j] > alist[max_index]:
                max_index = j
        alist[i], alist[max_index] = alist[max_index], alist[i]