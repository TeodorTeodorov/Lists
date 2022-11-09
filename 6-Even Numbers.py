numbers = list(map(int, input().split(", ")))
result = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(result)

