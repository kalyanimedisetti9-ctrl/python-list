list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged = []

for num in list1 + list2:
    if num not in merged:
        merged.append(num)

print(merged)