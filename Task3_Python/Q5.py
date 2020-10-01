List=[24,43,11,36,20,15]
print("original list= ", List)

for i in List:
    if(i%2 == 0):
        List.remove(i)

print("List after removing the Even Numbers= ", List)