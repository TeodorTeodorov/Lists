level_of_fire_sell_quantity = input().split('#')
amount_of_water = int(input())
effort = 0
total_fire = 0
cells_list = []
for symbol in level_of_fire_sell_quantity:
    element = symbol.split(' = ')
    type_fire = element[0]
    value_of_cell = int(element[1])
    if type_fire == 'High':
        if 81 < value_of_cell <= 125 and amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell + (value_of_cell * 0.25)
            total_fire += value_of_cell
            effort += value_of_cell * 0.25
            cells_list.append(value_of_cell)
        else:
            continue
    if type_fire == "Medium":
        if 51 < value_of_cell <= 80 and amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell + (value_of_cell * 0.25)
            total_fire += value_of_cell
            effort += value_of_cell * 0.25
            cells_list.append(value_of_cell)
        else:
            continue
    if type_fire == "Low":
        if 1 < value_of_cell <= 50 and amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell + (value_of_cell * 0.25)
            total_fire += value_of_cell
            effort += value_of_cell * 0.25
            cells_list.append(value_of_cell)
        else:
            continue
print('Cells:')
print(sep='\n - ', *cells_list)
print(f'Effort: {effort:.02f}')
print(f'Total Fire: {total_fire}')

