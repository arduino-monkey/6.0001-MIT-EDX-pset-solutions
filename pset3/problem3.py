def getAvailableLetters(lettersGuessed):
    alpha_lis = list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in alpha_lis:
            alpha_lis.remove(i)
    return "".join(alpha_lis)