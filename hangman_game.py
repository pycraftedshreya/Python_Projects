# Hangman game is guessing the word from given alphabet : rule - get 7 chances 
import random 
# words = ["UMBRELLA","COMPUTER","TELESCOPE","SMARTPHONE"]

# to get more words : 
f = open('words.txt','r') 
data = f.readline()     # get in list forms 
words = data.split()
select_word = random.choice(words)

total_chances = 7

# get the dash or blank spaces for words
guesses_word = "-"*len(select_word)

while total_chances != 0 :
    print(guesses_word)
    guess_letter = input("Guess a lettter : ").upper()
    
    if guess_letter in select_word:
        # for loop chalse aakha word ma 
        for index in range(len(select_word)):
            # guess kariyu che ae letter match thai che : 
            if select_word[index] == guess_letter:
                guesses_word = guesses_word[:index] + guess_letter+guesses_word[index+1:]
                print(guesses_word)
        if guesses_word == select_word:
            print("Congratulations you won !!")
            break 

    else : 
        total_chances -=1
        print("Incorrect Guess")
        print("The remaining chances are: ",total_chances)

else: 
    print("Game over ")
    print("Better Luck Next Time") 
    print("All the chances are exhausted ")
print("The correct word is :",select_word)