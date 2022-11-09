list_of_integer = input().split()
count_of_numbers_to_remove = int(input())
list_as_digit =[]
for element in list_of_integer:
    list_as_digit.append(int(element))
for check in range(count_of_numbers_to_remove):

    list_as_digit.remove(min(list_as_digit))

print(', '.join(map(str,list_as_digit)))



