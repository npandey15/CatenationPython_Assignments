
String="Consul12"
print("Expected Output: ", String)
l=d=0

for i in range(len(String)):
    if(String[i].isalpha()):
        l=l+1

    elif(String[i].isdigit()):
        d=d+1
    else:
        pass

print("Letters in String: ", l)
print("Digits in String: ", d)