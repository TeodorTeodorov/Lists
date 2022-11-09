number_of_electron = int(input())
filled_shell = []
while True:
    is_number_of_electron_even = True
    for shell in range(1, number_of_electron + 1):
        full_shell = 2*shell**2
        if number_of_electron > full_shell:
            number_of_electron -= full_shell
            filled_shell.append(full_shell)
        else:
            filled_shell.append(number_of_electron)
            is_number_of_electron_even = False
            break
    break

print(filled_shell)

