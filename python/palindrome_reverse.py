def palindrome_check(s):
    """  str -> Boolean

    Return 'True' if string is a palindrome:

    >>> palindrome_check('hello')
    False

    """
    return s == reverse_string(s)


def reverse_string(check):
    """
    str -> str
    reverse the order of the input string:

    >>> reverse_string('hello')
    'olleh'

    """
    reverse = ''

    for character in check:
        reverse = character + reverse

    return reverse

