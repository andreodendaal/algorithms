
def bubble_sort(L):
    '''
    Sort the list,
    :param L:
    :return:

    >>> L = [5, 4, 1, 7, 2]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 4, 5, 7]

    >>> L = [7, 5, 4, 2, 1]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 4, 5, 7]

    >>> L = [1, 2, 4, 5, 7]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 4, 5, 7]

    '''
    end = len(L) - 1

    while end != 0:

        for i in range(end):
            if L[i] >= L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
        end -= 1

