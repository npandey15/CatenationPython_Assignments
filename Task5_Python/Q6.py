x=open("doc.txt", "r")
a=x.read()
words=a.split()
for i in words:
    if len(i) % 2 == 0:
        print(i)
    