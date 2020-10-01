Counter=0

while Counter <= 5:
    Num=int(input("Guess the Lucky Num: "))

    if Num == 7:
        print("Good Guess")

    else:
        print("Try Again")
        Counter=Counter+1

    print("Game over")
    