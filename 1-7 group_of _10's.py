numbers = [int(num) for num in input().split(", ")]

group_list = 10
while numbers:
    num_start_group = [item for item in numbers if item <= group_list]
    numbers = [item for item in numbers if item > group_list]
    print(f"Group of {group_list}'s: {num_start_group}")
    group_list += 10

