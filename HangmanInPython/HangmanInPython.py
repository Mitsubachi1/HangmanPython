import random
from words import word_list

def get_word():
     word = random.choice(word_list)
     return word.upper()

def play(word):
    #variables
     hidden_word = "_" * len(word)
     guessed = False
     guessed_letters = []
     guessed_words = []
     tries = 6
     #displays general information: Intro, letters in the word, lives left, picture of hangman
     print("Welcome to hangman!") 
     print("You have a",len(word), "letter word")
     print(display_hangman(tries))
     print(hidden_word)
     print("\n")
     #Jumps into while loop for the actual game
     while not guessed and tries > 0:
         guess = input("Guess a letter or word: ").upper() #input is changed to uppercase to avoid case sensitive
         if len(guess) == 1 and guess.isalpha():
             if guess in guessed_letters:
                 print("You already guessed this", guess)
             elif guess not in word:
                 print(guess , "is not in the word.")
                 tries -= 1
                 guessed_letters.append(guess)
             else:
                 print("Correct!", guess, "is one of the letters!")
                 guessed_letters.append(guess)
                 word_as_list = list(hidden_word)
                 indices = [i for i, letter in enumerate(word) if letter == guess]
                 for index in indices:
                     word_as_list[index] = guess
                 hidden_word = "".join(word_as_list)
                 if "_" not in hidden_word:
                     guessed = True
    #if player attempts to guess the word in its entirety
         elif len(guess) == len(word) and guess.isalpha():
             if guess in guessed_words: #to prevent guessing words already guessed
                 print("You have already guessed the word", guess)
             elif guess != word:
                 print (guess, "is not the correct word.")
                 tries -= 1
                 guessed_words.append(guess)
             else:
                 guessed = True
                 hidden_word = word
         else: #to ignore inputs that are not letters
            print ("Not a valid guess.")
    #display information of game: photo of hangman, tries left, and hidden word
         print (display_hangman(tries))
         print (hidden_word)
         print ("You have", tries, "tries left.")
         print ("\n")
     if guessed:
        print("Congrats! you got the word:", word)
     else:
         print("Tough luck, you ran out of tries. The word we were looking for was "+ word)



#stages of hangman
def display_hangman(tries):
    stages = [ """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    / \\
                    --------
               """,
               """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    /  
                    --------
               """, 
               """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    
                    --------
               """,
               """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    
                    --------
               """,
               """
                    -------
                    |     |
                    |     O
                    |    \\|
                    |     |
                    |  
                    --------
               """,
               """
                    -------
                    |     |
                    |     O
                    |     |
                    |     
                    |    
                    --------
               """,
               """
                    -------
                    |     |
                    |     O
                    |    
                    |    
                    |    
                    --------
               """,
               """
                    -------
                    |     |
                    |   
                    |   
                    |   
                    |   
                    --------
               """
        ]
    return stages [tries]

def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        print("\n")
        word = get_word()
        play(word)
        

if __name__ == "__main__":
    main()