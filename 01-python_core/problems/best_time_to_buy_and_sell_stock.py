numbers = [7, 1, 5, 3, 6, 4]

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

lowest_price = numbers[0]

sell = 0

profit = 0

for price in numbers:

    if price < lowest_price:
        lowest_price = price

    new_profit = price - lowest_price

    if new_profit > profit:
        profit = new_profit
        sell = price

print("The Buy is: ", lowest_price)

print(f"The Sell is: {sell}")

print("The Profit is: ", profit)



