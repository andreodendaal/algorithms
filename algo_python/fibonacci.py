def fibbonacci(p_val, p_range):
    """
    :param p_stop:
    :param p_range:
    :return: list of fibonacci values

    -> p_range > 0: Calculate all the Fibonacci values for a range of numbers
    Give me the first 10 Fibonacci numbers
    >>> fibbonacci(0, 10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    -> p_val > 0: Calculate all the Fibonacci values between 0 and P_val
    Give me all the Fibonacci numbers up to 35
    >>> fibbonacci(37, 0)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    >>> fibbonacci(55, 0)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    >>> fibbonacci(1, 0)
    [0, 1, 1]

    >>> fibbonacci(0, 0)
    [0]

    """

    # initialize the sequence
    fib_list = [0, 1]

    # calculate the Fibonacci sequence for a range of numbers
    if p_range != 0:

        for i in range(p_range-2):
            fib_list.append(fib_list[i] + fib_list[-1])

    # calculate the Fibonacci sequence up to a certain value
    elif p_val != 0:

        ctr = 0
        while fib_list[ctr] < p_val:

            if (fib_list[ctr] + fib_list[ctr+1]) > p_val:
                break

            fib_list.append(fib_list[ctr] + fib_list[-1])
            ctr += 1
    else:
        return [0]

    return fib_list
