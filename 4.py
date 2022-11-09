numbers = input().split(', ')
numbers_list = []

for money in numbers:
    numbers_list.append(int(money))
count_of_beggar = int(input())
money_list = []
start_index = 0
while start_index < count_of_beggar:
    sum_for_current_beggar = 0
    for index in range(start_index, len(numbers_list), count_of_beggar):
        sum_for_current_beggar += numbers_list[index]
    money_list.append(sum_for_current_beggar)
    start_index += 1
print(money_list)
