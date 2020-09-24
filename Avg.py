# Python program to demonstrate 
# Break Statement 
# Continue statement

# Using while loop

print("This is the task for calculating Average of Marks")

Sub1=int(input("Enter the marks for Sub1: "))
Sub2=int(input("Enter the marks for Sub2: "))
Sub3=int(input("Enter the marks for Sub3: "))
Sub4=int(input("Enter the marks for Sub4: "))
Sub5=int(input("Enter the marks for Sub5: "))

totalmarks= Sub1 +Sub2 +Sub3 +Sub4 + Sub5

print("Total Marks = ", totalmarks)

num=int(input("how many subjects: "))

Average=(totalmarks)/5

while True:
    print("Average Marks = ", Average)

    if Average<0:
        print("Improve your marks")
        break

    if(Average>=90):
        print("Excellent")
        continue

    elif (Average>=50 and Average<=60):
        print("below Average")
        break
    
    elif (Average>=60 and Average<=70):
        print("Average")
        break

    elif (Average>=70 and Average<=80):
        print("Good")
        break
    
    elif (Average>=80 and Average<=90):
        print("Very good")
        break

print("Average marks for 5 Subjects, Congratulation!")
   
    

