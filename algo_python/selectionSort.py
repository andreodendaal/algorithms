def selectionSort_2(lst):
    """
    My solution to:

    https://runestone.academy/runestone/static/pythonds/SortSearch/TheSelectionSort.html

    Manipulating the same list

    >>> selectionSort_2([54,26,93,17,77,31,44,55,20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]

    >>> selectionSort_2([17,20,26,31,44,54,55,77,93])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]

    >>> selectionSort_2([54,26,93,17,54,77,31,44,55,20])
    [17, 20, 26, 31, 44, 54, 54, 55, 77, 93]

    :param lst:
    :return:
    """

    index = len(lst) - 1

    while index > 1:
        largest_val = 0
        for lst_position, value in enumerate(lst[:(index + 1)]):
            if value > largest_val and lst_position <= index:
                largest_val = value
        lst.remove(largest_val)
        lst.insert(index, largest_val)
        index -= 1

    return lst

def selectionSort_1(lst):

    """
    My solution to:

    https://runestone.academy/runestone/static/pythonds/SortSearch/TheSelectionSort.html

    Using a reference list

    >>> selectionSort_1([54,26,93,17,77,31,44,55,20])
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



def selectionSort_solution(alist):

    """

    >>> selectionSort_solution([11, 7, 12, 14, 19, 1, 6, 18, 8, 20])
    [20, 19, 18, 14, 12, 11, 8, 7, 6, 1]

    :param alist:
    :return:
    """

    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


