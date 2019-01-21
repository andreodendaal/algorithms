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

    # Total counter of records that are unsorted
    toProcess = len(lst) - 1

    while toProcess > 1:

        largest_val = 0

        # only iterate over the unsorted elements
        for lst_position, value in enumerate(lst[:(toProcess + 1)]):

            # get largest value, of unsorted elements.
            if value > largest_val and lst_position <= toProcess:
                largest_val = value

        # sort
        lst.remove(largest_val)
        lst.insert(toProcess, largest_val)

        # update the total of records left to sort
        toProcess -= 1
    return lst

def selectionSort_3(lst):
    """
    Researched solution to:

    https://runestone.academy/runestone/static/pythonds/SortSearch/TheSelectionSort.html

    Manipulated solution found at : https://www.geeksforgeeks.org/python-program-for-selection-sort/

    >>> selectionSort_3([54,26,93,17,77,31,44,55,20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]

    >>> selectionSort_3([17,20,26,31,44,54,55,77,93])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]

    >>> selectionSort_3([54,26,93,17,54,77,31,44,55,20])
    [17, 20, 26, 31, 44, 54, 54, 55, 77, 93]

    :param lst:
    :return:
    """
    for index in range((len(lst) - 1), 0, -1):

        biggest_idx = index
        for next_idx in range(biggest_idx):
            if lst[biggest_idx] < lst[next_idx]:
                biggest_idx = next_idx

        lst[index], lst[biggest_idx] = lst[biggest_idx], lst[index]

    return lst



def selectionSort_solution(alist):

    """

    >>> selectionSort_solution([11, 7, 12, 14, 19, 1, 6, 18, 8, 20])
    [1, 6, 7, 8, 11, 12, 14, 18, 19, 20]

    >>> selectionSort_solution([54, 26, 93, 17, 77, 31, 44, 55, 20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]

    :param alist:
    :return:
    """

    for fillslot in range(len(alist)-1, 0, -1):

        positionOfMax = 0

        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        # Refactor original solution
        #temp = alist[fillslot]
        #alist[fillslot] = alist[positionOfMax]
        #alist[positionOfMax] = temp

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


    return alist


