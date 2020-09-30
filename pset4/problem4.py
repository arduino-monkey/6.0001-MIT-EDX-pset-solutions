def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    numberOfLetters = 0
    for letter in hand.keys():
        numberOfLetters += hand[letter]
    return numberOfLetters