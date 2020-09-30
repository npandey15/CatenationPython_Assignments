
# Passwd creation in python

def checker_password(Passwd):
    "Check if Passwd is valid"
    Specialchar=["$","#","@","*","%"]
    return_val=True

    if len(passwd) < 8:
        print("Passwd is too short, length of the password should be at least 8")
        return_val=False

    if len(passwd) > 30:
        print("Passwd is too long, length of the password should not be greater than 8")
        return_val=False

    elif len(passwd) > 8 and len(passwd) <= 30:
        print("Passwd OK")
        return_val=True

    if not any(char.isdigit() for char in passwd):
        print("Passwd should have atleast one numerical input")
        return_val=False

    if not any(char.isupper() for char in passwd):
        print("Passwd should have at least one UPPERCASE Letter")
        return_val=False

    if not any(char in Specialchar for char in passwd):
        print("Passwd should have at least one Special character $#@*%")
        return_val=False

    if return_val:
        print("OK")
        return return_val

    else:
        print("Invalid Passwd")

print(checker_password.__doc__)
passwd=input("Enter the password: ")
print(checker_password(passwd))





    

    

