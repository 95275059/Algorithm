from Sort.random_sequence import generateRandomArray
from Sort.bubble_sorting import bubble_sorting, bubble_sorting_v2
from Sort.select_sorting import select_sorting
from Sort.insert_sorting import insert_sorting
from Sort.shell_sorting import shell_sorting
from Sort.merge_sorting import merge_sorting1
from Sort.quick_sorting import quick_sorting
from Sort.count_sorting import count_sorting

def bubble_sorting_test(alist):
    bubble_sorting(alist)
    print(alist)


def bubble_sorting_v2_test(alist):
    bubble_sorting_v2(alist)
    print(alist)


def select_sorting_test(alist):
    select_sorting(alist)
    print(alist)


def insert_sorting_test(alist):
    insert_sorting(alist)
    print(alist)


def shell_sorting_test(alist):
    shell_sorting(alist)
    print(alist)


def merge_sorting_test(alist):
    merge_sorting1(alist)
    print(alist)


def quick_sorting_test(alist):
    quick_sorting(alist)
    print(alist)

def count_sorting_test(alist):
    count_sorting(alist)
    print(alist)

if __name__ == '__main__':
    alist = generateRandomArray(6, 1, 10)
    print(alist)
    insert_sorting_test(alist)