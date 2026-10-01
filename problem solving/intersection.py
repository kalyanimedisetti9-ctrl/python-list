list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 6]
list3 = [3, 4, 7, 8]

result = []

for num in list1:
    if num in list2 and num in list3:
        result.append(num)

print(result)