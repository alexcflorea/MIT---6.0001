# Problem Set 2, hangman.py
# Name: Alex Florea
# Collaborators: Alex Florea
# Time spent: 8/10/2020 - 8/25/2020

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    x = 0
    for let in secret_word:
        if let in letters_guessed:
            x += 1
            
        if x == len(secret_word):
            return True
        
        else:
            continue
        
    if x != len(secret_word):
        return False
                


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guess = []

    for let in secret_word:
        if let in letters_guessed:
            guess.append(let)
            
        else:
            guess.append("_ ")
        
    return ''.join(guess)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    letters_not_guessed = string.ascii_lowercase
    
    for let in letters_guessed:
        if let in letters_not_guessed:
            letters_not_guessed = letters_not_guessed.replace(let, '')
            
    return letters_not_guessed

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")
    

    
    while guesses_remaining > 0:    
        print("-------------")
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed), end="")
        users_guess = str.lower(input("Please guess a letter: "))
                            
        if str.isalpha(users_guess) is True:
            if len(users_guess) > 1:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                
                else:
                    guesses_remaining -= 1
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            
            elif users_guess not in get_available_letters(letters_guessed):
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                
                else:
                    guesses_remaining -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                    
            else:
                if users_guess in secret_word:
                    letters_guessed.append(users_guess)
                    print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                    
                else:
                    if users_guess in vowels:
                       letters_guessed.append(users_guess)
                       guesses_remaining -= 2
                       print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                       
                    else:
                       letters_guessed.append(users_guess)
                       guesses_remaining -= 1
                       print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                 
        else: 
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                
        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = ""
            for let in secret_word:
                if let not in unique_letters:
                    unique_letters = unique_letters + let
                
            total_score = guesses_remaining * len(unique_letters)
            print("-------------")
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            break
        
    if guesses_remaining <= 0:         
        print("-------------")
        print("Sorry, you ran out of guesses. The word was", secret_word)
        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    my_word = list(my_word.replace('_ ','0'))
    other_word = list(other_word)
    
    if len(my_word) != len(other_word):
        return False
    
    else:
        for i in range(len(my_word)):
            if my_word[i] == other_word[i] and my_word.count(my_word[i]) != other_word.count(other_word[i]):
                return False
       
        for i in range(len(my_word)):
            if my_word[i] == '0':
                my_word[i] = ""
                other_word[i] = ""
                
        return my_word == other_word



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_words = []
    
    for word in wordlist:    
        if match_with_gaps(my_word, word):
            possible_words.append(word)
            
    if possible_words == []:
        print("No matches found")
        
    else:
        print(possible_words)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")
    

    
    while guesses_remaining > 0:    
        hint_used = False
        
        print("-------------")
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed), end="")
        users_guess = str.lower(input("Please guess a letter: "))
             
        if users_guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            hint_used = True
            
        if not hint_used:       
            if str.isalpha(users_guess) is True:
                if len(users_guess) > 1:
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                    
                    else:
                        guesses_remaining -= 1
                        print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                
                elif users_guess not in get_available_letters(letters_guessed):
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                    
                    else:
                        guesses_remaining -= 1
                        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                        
                else:
                    if users_guess in secret_word:
                        letters_guessed.append(users_guess)
                        print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                        
                    else:
                        if users_guess in vowels:
                           letters_guessed.append(users_guess)
                           guesses_remaining -= 2
                           print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                           
                        else:
                           letters_guessed.append(users_guess)
                           guesses_remaining -= 1
                           print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                 
            else: 
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                    
                else:
                    guesses_remaining -= 1
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                    
        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = ""
            for let in secret_word:
                if let not in unique_letters:
                    unique_letters = unique_letters + let
                
            total_score = guesses_remaining * len(unique_letters)
            print("-------------")
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            break
        
    if guesses_remaining <= 0:         
        print("-------------")
        print("Sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
