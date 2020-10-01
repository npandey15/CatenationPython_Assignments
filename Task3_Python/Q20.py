even_list=[2,6,12,14]
odd_list=[3,9,7,11]

for i in range(1,51) :
    x=int(input("Enter a number between 1 to 50:  "))
    if x%2==0:
        even_list.append(x)
        print("New even_list :  ", even_list)
        j=sum(even_list)
        print("Sum of the list is :  ", j)
        k=max(even_list)
        print("Maximum of the even_list is :  ", k)
        break

    if x%2!=0:
        odd_list.append(x)
        print("New odd_list is : ", odd_list)
        l=sum(even_list)
        print("Sum of the list :  ", l)
        m=max(even_list)
        print("Max of the odd_list :  ", m)
        break
