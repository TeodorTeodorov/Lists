gifts_for_buy = input().split()
command = input().split()
gifts_list = []
while command != "No Money":

    if 'OutOfStock' in command:

        if command[1] in gifts_for_buy:
            gifts_for_buy.remove(command[1])
    elif 'Required' in command:
        index = int(command[2])
        if 0 <= index < len(gifts_for_buy):
            gifts_for_buy.append(command[1])

    elif command[0] == 'JustInCase':
        gifts_for_buy.append(command[1])
    command = input().split()
print(' '.join(gifts_for_buy))



