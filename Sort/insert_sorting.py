def insert_sorting(alist):
    # 时间复杂度：平均：o(n**2)，最好：o(n)，最坏：o(n**2)
    # 空间复杂度：o(1)
    # 稳定性：稳定
    length = len(alist)
    for i in range(1, length):
        curnode = alist[i]
        position = i
        while position > 0 and alist[position-1] > curnode:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = curnode