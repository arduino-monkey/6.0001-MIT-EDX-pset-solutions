def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    game = True
    lastHand = {}
    while game:
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if choice == 'r':
            if lastHand == {}:
                print('You have not played a hand yet. Please play a new hand first!')
                print()
            else:
                playHand(lastHand,wordList,HAND_SIZE)
        elif choice == 'n':
            hand = dealHand(HAND_SIZE)
            lastHand = hand.copy()
            playHand(hand,wordList,HAND_SIZE)
        elif choice == 'e':
            game = False
        else:
            print('invalid command')