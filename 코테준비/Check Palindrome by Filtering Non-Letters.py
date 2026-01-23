def isAlphabeticPalindrome(code):
    NL=[]
    for x in code:
        if (x.isalpha() == True):
            NL.append(x.lower())
    for x in range(1,int(len(NL)/2)):
        if NL[x]!=NL[(x+1)*-1]:
            return 0
    return 1 
