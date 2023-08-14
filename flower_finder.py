from collections import deque

vowels = deque(a for a in input().split())
consonants = deque(b for b in input().split())

words = {"rose": "rose",
         "tulip": "tulip",
         "lotus": "lotus",
         "daffodil": "daffodil"}

word_found = ""

while not word_found and vowels and consonants:
    vowel = vowels.popleft()
    cons = consonants.pop()

    for key, value in words.items():
        if vowel in value:
            value = value.replace(vowel, "")
            words[key] = value
        if cons in value:
            value = value.replace(cons, "")
            words[key] = value

        if not words[key]:
            word_found = key
            break

if word_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(el for el in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(el for el in consonants)}")
