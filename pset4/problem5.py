def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    game = True
    points = 0
    while game and calculateHandlen(hand) != 0:
        print('Current Hand:',end = ' ')
        displayHand(hand)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        if word == ".":
            game = False
        else:
            if isValidWord(word,hand,wordList):
                wordScore = getWordScore(word,n)
                hand = updateHand(hand,word)
                points += wordScore
                print('"' + word + '"' ,'earned' , wordScore, 'points. Total:', points ,'points')
            else:
                print('Invalid word, please try again.')
            print()
            
    if calculateHandlen(hand) != 0:
        print('Goodbye! Total score:' , points , 'points.')
    else:
        print('Run out of letters. Total score:' , points ,'points.')
