numbers = []

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

result = set(numbers)

print(len(result) != len(numbers))
