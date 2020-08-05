def no_dups(s):
    # Your code here
    cache = {}
    sentence = ''
    s = s.split()
    for word in s:
        if word not in cache:
            cache[word] = word
    for key in cache.keys():
        sentence += str(key) + ' '
    print(sentence)
    return sentence.lstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
