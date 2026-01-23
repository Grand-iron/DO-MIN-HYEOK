def maxDistinctSubstringLengthInSessions(sessionString):
    if sessionString == '*':
        return 0
    c=[]
    count=0
    for x in sessionString:
        if x not in c and x != '*':
            c.append(x)
        else:
            if count <= len(c):
                count=len(c)
            c=[]
    return count