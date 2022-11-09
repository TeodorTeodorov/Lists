command = input()
lst_notes = [0] * 10
while command != 'End':
    command_split = command.split('-')
    importance = int(command_split[0])
    current_task = command_split[1]
    lst_notes.pop(importance)
    lst_notes.insert(importance, current_task)



    command = input()

result = [index for index in lst_notes if index != 0]

print(result)
