def adjacent(x):
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return True
    return False

def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while adjacent(s):
        result = ""
        for i in range(len(s)):
            if i < len(s)-1 and s[i] == s[i+1]:
                result += s[i+2:]
                break
            else:
                result += s[i]
        s = result
    return s