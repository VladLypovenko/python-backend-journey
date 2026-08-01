numbers = [0, 1, 0, 3]
while True:
    print("Please enter a number: ")
    try:
        value = int(input())

    except ValueError:
        continue

    numbers.append(value)

    print("One more? (y/n)")
    choice = input()

    choice = choice.lower()

    if choice != 'y':
        break

print(numbers)

read = 0

write = 0

count = 0

for item in numbers:

    if item != 0:
        numbers[write] = numbers[read]
        write += 1

    else:
        count += 1

    read += 1

for i in range(count):
    numbers[len(numbers) - 1 - i] = 0


print(numbers)
