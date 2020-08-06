def letter_count(s):
    d = {}

    for c in s:
        if c.isspace():
            continue
        c = c.lower()

        if c not in d:
            d[c] = 0
        d[c] += 1

        # print(c)
    return d


print(letter_count('hello'))


def print_sorted_count(s):
    d = letter_count(s)

    items = list(d.items())
    items.sort(key=lambda e: e[1], reverse=True)

    for i in items:
        print(f'{i[0]}: {i[1]}')


(print_sorted_count('We need to check if c is in the dictionary first'))
