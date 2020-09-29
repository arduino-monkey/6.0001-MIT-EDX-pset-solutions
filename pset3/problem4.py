def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    letters_list = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is' , len(secretWord) , 'letters long')
    print(13*'-')
    while guesses >= 1 and isWordGuessed(secretWord,letters_list) == False:

        print('You have', guesses,'guesses left')
        print('Available letters:',getAvailableLetters(letters_list))
        guessed_letter = input('Please guess a letter: ').lower()
        
        if guessed_letter.isalpha() and guessed_letter not in letters_list:
            letters_list.append(guessed_letter)
            if guessed_letter in secretWord:
                print('Good guess:',getGuessedWord(secretWord,letters_list))
            else:
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord,letters_list))
                
                if guessed_letter in 'aeiou':
                    guesses -= 1
                else:
                    guesses -= 1
            
        elif guessed_letter.isalpha() and guessed_letter in letters_list:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,letters_list))
            
        print(13*'-')
    if isWordGuessed(secretWord,letters_list) == True:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was',secretWord+'.')