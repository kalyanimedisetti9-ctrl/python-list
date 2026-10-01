numbers = [4, 5, 1, 2, 5, 1, 3]

seen = []

for num in numbers:
    if num in seen:
        print("First repeating element:", num)
        break
    seen.append(num)