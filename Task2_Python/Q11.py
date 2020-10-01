Counter=0

while Counter <= 5:
    Num=int(input("Guess the Lucky Num: "))

    if Num == 7:
        print("Good Guess!")
        break
    
    elif Num == " ":
        print("Sorry but that was not successful!")

    else:
        print("Try Again once more!")
        Counter=Counter+1


    