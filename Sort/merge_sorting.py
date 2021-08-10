def merge_sorting1(alist):
    # 归并排序
    # 自顶向下递归方法
    # 采用分治法的思想
    # 时间复杂度:平均：o(nlog2(n)),最坏：o(nlog2(n)),最好：o(nlog2(n)),
    # 空间复杂度：o(n)
    # 稳定性：稳定
    length = len(alist)
    _merge_sorting1(alist, 0, length-1)


def _merge_sorting1(alist, start_index, end_index):
    if start_index >= end_index:
        return
    mid = start_index + (end_index - start_index) // 2
    _merge_sorting1(alist, start_index, mid)
    _merge_sorting1(alist, mid+1, end_index)
    #优化
    if alist[mid] > alist[mid+1]:
        merge(alist, start_index, mid, end_index)


def merge(alist, start_index, mid, end_index):
    blist = alist[start_index: end_index+1]
    curnode_index = start_index
    i, j = start_index, mid + 1
    while curnode_index <= end_index:
        if i > mid:
            alist[curnode_index] = blist[j - start_index]
            j += 1
        elif j > end_index:
            alist[curnode_index] = blist[i - start_index]
            i += 1
        elif blist[i - start_index] >= blist[j - start_index]:
            alist[curnode_index] = blist[j - start_index]
            j += 1
        else:
            alist[curnode_index] = blist[i - start_index]
            i += 1
        curnode_index += 1