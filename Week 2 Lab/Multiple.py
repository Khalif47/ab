# Input

def insertion(alist):
    n = len(alist)
    for i in range(1, n):
        target = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > target:
            alist[j + 1] = alist[j]
            j = j - 1
            alist[j + 1] = target
    return alist


def shakersort(alist):
    n = len(alist)
    swapped = False
    for i in range(n - 1, 0, -1):
        if i % 2 == 0:
            for j in range(i):
                if alist[j + 1] < alist[j]:
                    alist[j + 1], alist[j] = alist[j], alist[j + 1]
                    swapped = True
            if not swapped:
                break
        else:
            for j in range(i - 1, -1, -1):
                if alist[j] < alist[j-1]:
                    alist[j + 1], alist[j] = alist[j], alist[j + 1]
                    swapped = True
            if not swapped:
                break

    return alist


print(shakersort([3, 2, 5, 3, 2, 0, -1, 3]))
