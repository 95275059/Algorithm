from random import randint
def quick_sorting(alist):
    # 时间复杂度:平均：o(nlog2(n))，最慢：o(n**2)，最快：o(nlog2(n))，
    # 当每次待排序子数列已经有序(升序或降序时)，快排最慢
    # 空间复杂度：o(nlog2(n))
    # 稳定性：不稳定
    length = len(alist)
    _quick_sorting(alist, 0, length-1)

def _quick_sorting(alist, start_index, end_index):
    if start_index >= end_index:
        return
    p = find_index(alist, start_index, end_index)
    _quick_sorting(alist, start_index, p - 1)
    _quick_sorting(alist, p + 1, end_index)

def find_index(alist, start_index, end_index):
    rand_index = randint(start_index, end_index)
    alist[start_index], alist[rand_index] = alist[rand_index], alist[start_index]
    v = alist[start_index]
    i, index = start_index + 1, start_index
    while i <= end_index:
        if alist[i] <= v:
            alist[index+1], alist[i] = alist[i], alist[index+1]
            index += 1
        i += 1
    alist[start_index], alist[index] = alist[index], alist[start_index]
    return index