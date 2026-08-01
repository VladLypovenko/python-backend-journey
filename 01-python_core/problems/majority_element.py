numbers = [1,1,2,2,2,2,3,4]

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


seen = {}

for number in numbers:
    if number not in seen:
        seen[number] = 1

    else:
        seen[number] += 1

    if seen[number] > len(numbers) / 2:
        print(f"The number {number} is Majority")
        quit()

for key,value in seen.items():
    if value > len(numbers) / 2:
        print(f"The number {key} is Majority")
        quit()

print("There are no Majority numbers")