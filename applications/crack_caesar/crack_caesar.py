# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
forbiddenCharacters = ['"', ':', ';', ',', '.', '-', '+', '=',
                       '/', '|', '[', ']', '{', '}', '(', ')' '*', '^', '&', '\\', ' ', '!', "'", '\n', '?']

wordCount = {}
totalCount = 0
with open('ciphertext.txt') as text:
    jumble = text.read()
    text.close()
# print(jumble)
for q in jumble:
    # print(q)
    for r in forbiddenCharacters:
        if r == q:
            q = q.replace(r, '')
    if q not in wordCount:
        wordCount[q] = 0
    wordCount[q] += 1
    totalCount += 1
wordCount = list(wordCount.items())
wordCount.sort(key=lambda e: e[1], reverse=True)
wordCount.pop(0)
print(wordCount)
print(totalCount)

mostUsedLetters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L',
                   'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
decipher = {}
y = 0
while y is not len(mostUsedLetters):
    # print(mostUsedLetters[y])
    # print(wordCount[y])
    decipher[wordCount[y][0]] = mostUsedLetters[y]
    y += 1
for w in jumble:
    if w not in decipher:
        decipher[w] = w
    else:
        continue

print(jumble)
print(decipher)
paragraph = ''
for letter in jumble:
    r += decipher[letter]
print(r)
