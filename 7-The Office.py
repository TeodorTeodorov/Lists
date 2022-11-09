happiness = list(map(int,input().split(" ")))
factor = int(input())
improvement_list = []
for num in happiness:
    improvement = num * factor
    improvement_list.append((improvement))
print(improvement_list)
filtered_improvement_list = list(filter(lambda x: x >= (sum(improvement_list) / len(improvement_list)), improvement_list))
print(filtered_improvement_list)
if len(filtered_improvement_list) >= len(improvement_list) / 2:
    print(f'{len(filtered_improvement_list)} / {len(improvement_list)} happy')
else:
    print("not happy")