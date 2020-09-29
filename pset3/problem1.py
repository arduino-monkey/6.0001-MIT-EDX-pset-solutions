def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        for j in lettersGuessed:
            if i==j:
                break
        else:
            return False
    else:
        return True