import random 
word_list=["kia","gucci","olukai","coffee"] #list of words
result=random.choice(word_list) 
print(word_list)
print(result)

guessed_letters=[] 
used_letters=[]

initial_word_view=list("_"*len(result))   #replace length with _
num_correct_letters=0
incorrect_guesses=4 

while num_correct_letters<len(result) and incorrect_guesses>0:
    guess=input("Enter your selection: ")
    print(initial_word_view) 

    if guess in result:
        print("Your guessed letter {} in the word | {} | is correct".format(guess, guessed_letters))
        print("".join(initial_word_view))
        for a in range(len(result)):
            if result[a]==guess:
                initial_word_view[a] = guess
        else:
            #print("Your guessed letter {} in the word | {} | is incorrect".format(guess, guessed_letters))
            print("Guess the next letter!")

        if num_correct_letters==len(result):
            print("Congrats! you guessed the correct word.") 
    else:
        print("You lost!")