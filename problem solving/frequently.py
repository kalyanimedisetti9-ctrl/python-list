numbers = [1, 2, 2, 3, 2, 4, 3]

most_frequent = numbers[0]

for num in numbers:
    if numbers.count(num) > numbers.count(most_frequent):
        most_frequent = num

print("Most frequent element:", most_frequent)