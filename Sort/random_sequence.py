from random import randint


def generateRandomArray(n, min, max):
    arr = [randint(min, max) for _ in range(n)]
    return arr