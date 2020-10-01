# Printing vowels with index
def Check_Vow(string, vowels): 
      
    count = {}.fromkeys(vowels, 0) 
      
    # To count the vowels 
    for character in string: 
        if character in count: 
            count[character] += 1    
    return count 
      
vowels = 'aeiou'
string = "Consultadd Training Python"
print (Check_Vow(string, vowels))

