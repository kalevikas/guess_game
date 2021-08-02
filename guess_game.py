# Program to make guessing game.
secret_name= "Python"
Guess=""
guess_count=0
guess_count_limit=3
guess_out_of_limit=False

while Guess !=secret_name and not(guess_out_of_limit):
    if guess_count < guess_count_limit:
        Guess = input("Enter a name: ")
        guess_count+=1

    else:
        guess_out_of_limit=True

if guess_out_of_limit:
    print("Guess out of limit: You Loose!")
else:
    print("You Win!")