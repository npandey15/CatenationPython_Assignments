def showNumbers(limit):
    for i in range(0, limit):
        if i % 2 == 0 :
            print(i, "EVEN")
        elif i % 2 != 0:
            print(i, "ODD")

limit =int(input("Limit is:"))
showNumbers(limit)