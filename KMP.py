def get_next(ps):
    next = [0 for i in range(len(ps))]
    j, k = 0, -1
    next[0] = -1
    while j<len(ps) - 1:
        if k == -1 or ps[j] == ps[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[k]
    print(next)
    return next

def KMP(ts, ps):
    i, j = 0, 0
    next = get_next(ps)
    while i<len(ts) and j<len(ps):
        if j == -1 or ts[i] == ps[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(ps):
        return i-j
    else:
        return -1


if __name__ == '__main__':
    ts = "ABACBCDHI"
    ps = "ABAB"
    print(KMP(ts, ps))