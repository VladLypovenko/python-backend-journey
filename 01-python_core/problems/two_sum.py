
numbers = [2,7,-1,10]

work = True

while work:

    print("Enter a number: ")
    number = int(input())
    numbers.append(number)

    print("Add one more number?(y/n): ")

    answer = input()

    if answer != "y":
        work = False

    else:
        continue

print(numbers)

target = int(input("Enter a target number: "))

seen = {}

result = []

for i in range(0,len(numbers)):
    needed = target - numbers[i]

    if needed in seen:
        result.append(i)
        result.append(seen[needed])
        print([seen[needed], i])
        break
    else:
        seen[numbers[i]] = i

