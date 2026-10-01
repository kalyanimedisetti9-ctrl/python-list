numbers = [1, 2, 2, 3, 3, 3, 4]

least_frequent = numbers[0]

for num in numbers:
    if numbers.count(num) < numbers.count(least_frequent):
        least_frequent = num

print("Least frequent element:", least_frequent)