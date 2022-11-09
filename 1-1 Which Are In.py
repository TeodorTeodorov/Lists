first_sequences = input().split(", ")
second_sequences = input().split(", ")
result = [word for word in first_sequences if any(word2 for word2 in second_sequences)]
print(result)




# substrings = []
# for word in first_sequences:
#     for word2 in second_sequences:
#         if word in word2:
#             substrings.append(word)
#             break
# print(substrings)