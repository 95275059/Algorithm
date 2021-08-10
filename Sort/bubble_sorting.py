def bubble_sorting(alist):
    # 时间复杂度：o(n**2),空间复杂度：o(1)
    # 空间复杂度：o(1)
    # 稳定性：稳定
    length = len(alist)
    for i in range(length-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


def bubble_sorting_v2(alist):
    # 时间复杂度：平均：o(n**2)，最好：o(n)，最坏：o(n**2)
    # 空间复杂度：o(1)
    length = len(alist)
    for i in range(length-1, 0, -1):
        changed = False
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                changed = True
        if not changed:
            break
