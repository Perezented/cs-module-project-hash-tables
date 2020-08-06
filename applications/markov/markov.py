import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # print(words)

followingWords = {}
# TODO: analyze which words can follow other words
# Your code here
# print(words)
filler = words.split()
i = 0
while i != len(filler)-1:
    print(filler[i])
    i += 1
    followingWords[filler[i]] = filler[i]
# TODO: construct 5 random sentences
# Your code here
