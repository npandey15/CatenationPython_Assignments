print("Enter a hyphen separated sequence of words:")
list=[n for n in raw_input().split('-')]  
list.sort()
print("Sorted:")
print('-'.join(list))