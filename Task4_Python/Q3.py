# function to get unique list value

def unique(list1):

    unique_list=[]

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

    for x in unique_list:
        print(x),

list1=[1,2,1,1,3,4,4,3,5]
print("The unique values from 1st list is")
unique(list1)