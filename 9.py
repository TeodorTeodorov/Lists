items_with_prices = input().split('|')
budget = float(input())
ticket = 150
profit_clothes = 0
profit_shoes = 0
profit_acsessories = 0
start_budget = budget
profit_for_print = []

for item in items_with_prices:
    event_item = item.split('->')
    type_of_item = event_item[0]
    item_value = float(event_item[1])
    if type_of_item == 'Clothes':
        if budget > item_value and item_value <= 50:
            budget -= item_value
            profit_clothes += item_value * 1.4
            profit_for_print.append("{:.2f}".format(item_value * 1.4))
    elif type_of_item == "Shoes":
        if budget > item_value and item_value <= 35:
            budget -= item_value
            profit_shoes += item_value * 1.4
            profit_for_print.append("{:.2f}".format(item_value * 1.4))
    elif type_of_item == "Accessories":
        if budget > item_value and item_value <= 20.5:
            budget -= item_value
            profit_acsessories += item_value * 1.4
            profit_for_print.append("{:.2f}".format(item_value * 1.4))

profit = budget + profit_clothes + profit_shoes + profit_acsessories

total_profit = profit - start_budget

if profit >= ticket:
    print(*profit_for_print)

    print(f'Profit: {total_profit:.02f}')
    print('Hello, France!')
else:
    print(*profit_for_print)
    print(f'Profit: {total_profit:.02f}')
    print("Not enough money.")
