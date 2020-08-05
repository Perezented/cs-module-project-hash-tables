"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


multiples = {}
for num in q:
    multiples[num] = f(num)
print(multiples)

for key0, value0 in multiples.items():
    for key1, value1 in multiples.items():
        print(key0, value0, key1, value1)

multiples_reversed = {value: key for (key, value) in multiples.items()}
print(multiples_reversed)

for key0, value0 in multiples_reversed.items():
    for key1, value1 in multiples_reversed.items():
        print(key0, value0, key1, value1)
