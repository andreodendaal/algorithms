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
