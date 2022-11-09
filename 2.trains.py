number = int(input())
train = [0] * number
command = input()
while True:

    if command == "End":
        break
    command = command.split(' ')
    if command[0] == 'add':
        train[-1] += int(command[1])
    elif command[0] == 'insert':
        train[0] += int(command[2])

    elif command[0] == 'leave':
        train[0] -= int(command[2])
    command = input()
print(train)


