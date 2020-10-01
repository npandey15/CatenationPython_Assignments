a="12abcbacbaba344ab"
b=filter(lambda a: a.isalpha(), "12abcbacbaba344ab")

freq={}

for i in b:
    if i in freq:
        freq[i]+=1 
        
    else:
        freq[i]=1
print(freq)
