def word_count(s):
    # Your code here
    forbiddenCharacters = ['"', ':', ';', ',', '.', '-', '+', '=',
                           '/', '|', '[', ']', '{', '}', '(', ')' '*', '^', '&', '\\']
    d = {}
    s = s.lower()
    for i in forbiddenCharacters:
        s = s.replace(i, '')
    s = s.split()
    for word in s:
        if word not in d:
            d[word] = 0
        d[word] += 1
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
