import random
import math
# Your code here


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    # v = math.pow(x, y)  # x ^ y
    # v = math.factorial(v)  # v is v *v-1 * v-2 * v-3 ... until 1
    # v //= z  # new number after is divided by x + y
    # v %= modMe  # moduloed by that num
    if (x, y) not in cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[x, y] = v
    return cache[x, y]
    # w = 1
    # u = 1

    # for i in range(y):
    #     w *= x
    # for i in range(1, w):
    #     u *= i
    #     v = u
    # v //= z
    # v %= modMe
    # cache[(x, y)] = v
    # print(f'~~~cache here: {cache}')


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')


# 5, 4 624454993
# 5, 3 179017319
#      179017319
#      476581239
