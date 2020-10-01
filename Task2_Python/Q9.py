while True :
    guess=int(input("Guess the Lucky Number: "))
    a="Yes"
    b="No"
    if guess == 13 :
        print("You guessed it right")
        break
    if guess != 13 :
        ask=str(input("Try again? Yes/No: "))
        if ask == a :
            continue
        if ask == b :
            break
        else :
            continue   

print("No more Guesses!")