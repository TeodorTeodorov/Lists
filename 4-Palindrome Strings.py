string = input().split(' ')
palindrome = input()
palindrome_list = []
for word in string:
    if word == word[::-1]:
        palindrome_list.append(word)
print(palindrome_list)

result = palindrome_list.count((palindrome))
print(f"Found palindrome {result} times")