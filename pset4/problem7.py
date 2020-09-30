def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    game = True
    lastHand = {}
    while game:
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        print()
        
        
    
        while lastHand == {} and choice == 'r':
            print('You have not played a hand yet. Please play a new hand first!')
            choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            
        
        
        
        
        if choice == 'r' and lastHand == {}:
            print('You have not played a hand yet. Please play a new hand first!')
            choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if choice == 'r' or choice == 'n':
            player = input('Enter u to have yourself play, c to have the computer play: ')
            print()
            while True:
                if player == 'u' or player == 'c':
                    break
                else:
                    print('invalid command')
                    print()
                    player = input('Enter u to have yourself play, c to have the computer play: ')
                
        
        if choice == 'r':
            if player == 'u':
                if lastHand == {}:
                    print('You have not played a hand yet. Please play a new hand first!')
                    print()
                else:
                    playHand(lastHand,wordList,HAND_SIZE)
            else:
                if lastHand == {}:
                    print('You have not played a hand yet. Please play a new hand first!')
                    print()
                else:
                    compPlayHand(lastHand,wordList,HAND_SIZE)
        
        elif choice == 'n':
            if player == 'u':
                hand = dealHand(HAND_SIZE)
                lastHand = hand.copy()
                playHand(hand,wordList,HAND_SIZE)
            else:
                hand = dealHand(HAND_SIZE)
                lastHand = hand.copy()
                compPlayHand(hand,wordList,HAND_SIZE)
        elif choice == 'e':
            game = False
        else:
            print('invalid command')
