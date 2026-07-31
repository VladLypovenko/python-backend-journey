print("Enter the first word: ")

first = input()

print("Enter the second word: ")

second = input()

if len(first) != len(second):
    print("First word and second word must have same length")
    quit()

seen = {}

for f,s in zip(first, second):
    if f not in seen:
        seen[f] = 1

    else:
        seen[f] += 1

    if s not in seen:
        seen[s] = -1

    else:
        seen[s] -= 1

for key in seen:
    if seen[key] != 0:
        print("Two words are not a valid anagrams")
        quit()

print("Two words are valid anagrams")
