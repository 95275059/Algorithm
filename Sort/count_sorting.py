def count_sorting(alist):
    # 计数排序不是基于比较的排序算法
    # 其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中
    # 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
    # 时间复杂度：平均：o(n+k), 最多：o(n+k)，最少：o(n+k),
    # 空间复杂度：o(n)
    # 稳定性：稳定
    if len(alist) < 2:
        return
    length = len(alist)
    minvalue, maxvalue = alist[0], alist[0]
    for i in alist:
        if i > maxvalue:
            maxvalue = i
        if i < minvalue:
            minvalue = i
    d = maxvalue - minvalue + 1
    temp = [0] * d
    for i in alist:
        temp[i - minvalue] += 1
    k = 0
    for i, num in enumerate(temp):
        for j in range(num):
            alist[k] = i + minvalue
            k += 1