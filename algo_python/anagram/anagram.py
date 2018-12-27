import string
def checking_off(s1,s2):
    anagram = True
    checklist = list(s2.lower())

    if len(s1) != len(s2):
        anagram = False

    for i in s1.lower():
        if i not in checklist:
            anagram = False

    return anagram


def sorting(s1, s2):

    list_1 = list(s1.lower())
    list_1.sort()
    list_2 = list(s2.lower())
    list_2.sort()

    return list_1 == list_2


def anagramSolution1(s1,s2):
    """
    Solution given in
    https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html?lastPosition=1423.4666748046875
    """
    #AO Moved True assertion to top of function
    stillOK = True

    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2)

    pos1 = 0
    #Lenght check will never work in original solution
    #AO stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

def anagramSolution4(s1,s2):
    """Count and compare
    From: https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html#solution-2-sort-and-compare

    >>> anagramSolution4('azzle','zleaz')
    True

    !does not account for uppercase
    """
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        val1 = ord(s1[i])
        val2 = ord('a')
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

def count_and_compare(s1, s2):
    """Count and compare
    >>> count_and_compare('azZle','zleaz')
    True
    >>> count_and_compare('azble','zleaz')
    False

    """

    ref_dict = dict((key, ctr) for ctr, key in enumerate(string.ascii_lowercase, start=1))
    total_s1 = 0
    total_s2 = 0

    for i in s1.lower():
        total_s1 += ref_dict[i]

    for i in s2.lower():
        total_s2 += ref_dict[i]

    return total_s1 == total_s2




