##hangman game
import random
word_list=['cat','dog','bird','tiger','lion','elephant','monkey','giraffee']
guessed_letters=[]
guesses_left=6
word_to_guess=random.choice(word_list)
word_length=len(word_to_guess)
hidden_word=list("_"*word_length)
while gusses_left>0:
    print(f"\n you have {gusses_left} guesses left.")
    print(f"the word is {"".join(hidden_word)}")
    print(f"you have guessesd : {",".join(guessed_lettes)}")
    guess=input("enter a letter :").lower()
    if guess in word_to_guess:
        indices=[i for i,x in enumerate(word_to_guess)if x==guess]
        for index in indices:
            hidden_word=[index]=guess
        if "_" not in hidden_word:
            print("\n Congratulations
            print(hidden_word)
            break
    else:
        guesses_left=1
        if guesses_left ==0:
            print(
            print(
            break
        guess
        
