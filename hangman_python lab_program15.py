import random
word_list=["dog","cat","tiger","lion","elephant","giraffe","monkey","bird"]
guessed_words=[]
guess_left=6
word_to_guess=random.choice(word_list)
word_length=len(word_to_guess)
hidden_word=list("_"*word_length)
while guess_left>0:
    print(f"You have {guess_left} guess left")
    print("You have guessed",' '.join(guessed_words))
    print("Your word is",' '.join(hidden_word))
    guess=input("Enter a letter:").lower()
    if guess in word_to_guess:
        indices=[i for i,x in enumerate(word_to_guess) if x==guess]
        for index in indices:
            hidden_word[index]=guess
        if "_" not in hidden_word:
            print("congradulation you wonn the game")
            print("Your word is ",word_to_guess)
            break
    else:
        guess_left-=1
        if guess_left==0:
            print("sorry no more guess left")
            print("Your word is ",word_to_guess)
            break
    guessed_words.append(guess)
    
