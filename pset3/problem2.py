def getGuessedWord(secretWord, lettersGuessed):
    lis = []
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            lis.insert(i,secretWord[i])
        else:
            lis.insert(i,'_ ')
    return "".join(lis)