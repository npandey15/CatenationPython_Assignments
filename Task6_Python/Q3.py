def count_upper_case_letters(str_obj):
    count = 0
    for elem in str_obj:
        if elem.isupper():
            count += 1
    return count
count = count_upper_case_letters('This is a Sample Text')
print(count)