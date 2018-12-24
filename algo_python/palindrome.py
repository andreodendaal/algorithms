def palindrome_reverse_full(s):
    """  str -> Boolean
    
    reverse the entire string and compare 

    Return 'True' if string is a palindrome:

    >>> palindrome_reverse_full('hello')
    False

    >>> palindrome_reverse_full('racecar')
    True
    """
    return s == reverse_string(s)


def palindrome_reverse_half(s):
    """  str -> Boolean

    Return 'True' if first half of the string == second half of the string reversed:

    >>> palindrome_reverse_half('hello')
    False
    
    >>> palindrome_reverse_half('dented')
    False
    
    >>> palindrome_reverse_half('racecar')
    True
    
    >>> palindrome_reverse_half('oooootooooo')
    True

    """
    segment = len(s)//2

    segment_start = s[:segment]

    segment_end = s[segment + 1:]
    segment_end_reverse = reverse_string(segment_end)

    return segment_end_reverse == segment_start


def compare_characters(S):
    """
    str -> boolean
    compare each character at the beginning of the string with counterpart at the end:
    
    >>> compare_characters('hello')
    False
    
    >>> compare_characters('dented')
    False
    
    >>> compare_characters('racecar')
    True
    
    >>> palindrome_reverse_half('oooootooooo')
    True

    """
    split = len(S)//2
    ctr_forward = 0
    ctr_back = -1
    while ctr_forward <= split:

        if S[ctr_forward] != S[ctr_back]:
            return False

        ctr_forward += 1
        ctr_back -= 1

    return True

def reverse_string(check):
    """
    str -> str
    reverse the order of the input string:

    >>> reverse_string('hello')
    'olleh'
    
    >>> reverse_string('racecar')
    'racecar'
    
    >>> reverse_string('a')
    'a'

    """
    reverse = ''

    for character in check:
        reverse = character + reverse

    return reverse

