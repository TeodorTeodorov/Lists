secret_message = input().split(' ')
full_list = []
list_1 = []
list_2 = []
list_3 = []
for index, word in enumerate(secret_message):
    int_list = []
    str_list = []
    for char in word:
        if char.isdigit():
            int_list.append(char)
        else:
            str_list.append(char)

    str_list[0], str_list[-1] = str_list[-1], str_list[0]
    int_list = "".join(int_list)
    str_int_list = chr(int(int_list))
    new_list = str_int_list + "".join(str_list)
    secret_message[index] = new_list

print(*secret_message)

# for char2 in secret_message2:
#     if char2.isdigit():
#         int_list2.append(char2)
#     else:
#         str_list2.insert(0, char2)
#
# int_list2 = "".join(int_list2)
# str_int_list2 = chr(int(int_list2))
# new_list2 = str_int_list2 + "".join(str_list2)
#
#
# for char3 in secret_message3:
#     if char3.isdigit():
#         int_list3.append(char3)
#     else:
#         str_list3.insert(0, char3)
#
#
# int_list3 = "".join(int_list3)
# str_int_list3 = chr(int(int_list3))
# new_list3 = str_int_list3 + "".join(str_list3)

