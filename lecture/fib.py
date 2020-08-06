# 0 1 1 2 3 5 8 13 21 34

cache = {}


def fib(n):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]
    # return fib(n-1) + fib(n-2)


for i in range(10000):
    print(f'{i:3}: {fib(i)}')


# def abc(x, y):
#     if (x, y) not in cache:


# items.sort(key=lambda e: e[1])
