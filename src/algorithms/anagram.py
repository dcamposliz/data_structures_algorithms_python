def anagram(s1, s2):

    # stripping out spaces
    s1_ = s1.replace(' ','').lower()
    s2_ = s2.replace(' ','').lower()

    # checking length
    if len(s1) != len(s2):
        return False
    
    # ---------------------------------------
    # ALTERNATE SOLUTION (Python specific):
    # return sorted(s1) == sorted(s2)
    # ---------------------------------------

    # character count dictionary
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False
    
    return True
        