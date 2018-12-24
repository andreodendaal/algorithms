def checking_off(s1,s2):
    anagram = True
    checklist = list(s2.lower())

    if len(s1) != len(s2):
        anagram = False

    for i in s1.lower():
        if i not in checklist:
            anagram = False

    return anagram
