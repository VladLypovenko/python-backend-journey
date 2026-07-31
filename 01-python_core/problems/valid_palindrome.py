print("Enter the sentence: ")

sentence = input()

sentence = sentence.lower()

symbols = [" ", ",", ":", ".", ";", "?"]

for symbol in symbols:
    if symbol in sentence:
        sentence = sentence.replace(symbol, "")

left = 0
right = len(sentence) - 1

while left < right:
    if sentence[left] != sentence[right]:
        print("Not a palindrome")
        quit()
    else:
        left += 1
        right -= 1


print("Palindrome")
