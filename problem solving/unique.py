numbers = [1, 2, 3, 2, 4, 5, 3, 6]

unique = []

for num in numbers:
    if numbers.count(num) == 1:
        unique.append(num)

print(unique)