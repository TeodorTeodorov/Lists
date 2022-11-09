factor = int(input())
count = int(input())
list_number = []
for number in range(1, count + 1):
    current_number = number * factor
    list_number.append(current_number)
print(list_number)
