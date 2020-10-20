while True:
    try:
        n =input("Please enter a Number: ")
        if len(n)>4 or len(n)<4:
            raise ValueError      
    except:
        print("Please length is too short/long!!! Please provide only four digits")
    
    else:
        if n==4:
            print("Great The Number is acceptable")
            break


