current_version = input().split('.')
current_version_int = [int(x) for x in current_version]
current_version_int[-1] += 1
for index in range(len(current_version_int) - 1, -1, -1):
    if current_version_int[index] > 9:
        current_version_int[index] = 0
        if index - 1 >= 0:
            current_version_int[index - 1] +=1
print('.'.join(str(number) for number in current_version_int))

