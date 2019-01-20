def selectionSort(lst):

    """
    My solution to:

    https://runestone.academy/runestone/static/pythonds/SortSearch/TheSelectionSort.html

    >>> selectionSort([54,26,93,17,77,31,44,55,20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]

    :param lst:
    :return:
    """
    lst_sorted = []
    ctr_end = 0
    scan_lst = lst[:]
    for _ in enumerate(lst):

        largest_val = 0
        for scan_ctr, scan_val in enumerate(scan_lst):
            if scan_val > largest_val:
                largest_val = scan_val

        lst_sorted.insert(ctr_end, largest_val)
        ctr_end -= 1
        scan_lst.remove(largest_val)

    return lst_sorted


