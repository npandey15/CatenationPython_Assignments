
# Program to perform operator based task

x=int(input("Please enter First number : "))
y=int(input("Please second second Number : "))

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def Avg(x + y / 2):
    return x + y/ 2

print("Select Operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print("5.Average")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ("1", "2", "3", "4", "5"):
        x=int(input("Please enter First number : "))
        y=int(input("Please Enter second Number : "))

        if choice == "1":
            print(x, "+", y,"=", Addition(x,y))
        
        elif choice == "2":
            print(x, "-", y, "=", Subtraction(x, y))

        elif choice == "3":
            print(x, "*", y, "=", Division(x, y))

        elif choice == "4":
            print(x, "/", y, "=", Multipicatiion(x, y))

        elif choice == "5":
            print(x, "((x + y)/2)", y, "=", Average(x, y))
            break
        else:
            print("Invalid Input")

        

