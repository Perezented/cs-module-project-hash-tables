# Your code here
cache = {}
forbiddenCharacters = ['"', ':', ';', ',', '.', '-', '+', '=',
                       '/', '|', '[', ']', '{', '}', '(', ')' '*', '^', '&', '\\']
with open('robin.txt') as f:
    words = f.read()
    f.close()
words = words.split()
for item in words:
    item = item.lower()
    for i in forbiddenCharacters:
        item = item.replace(i, '')
    print(item)
    if item not in cache:
        cache[item] = 0
    cache[item] += 1

cache = list(cache.items())
cache.sort(key=lambda e: e[1], reverse=True)
print(cache)
i = 0
lin = len(cache)
while i is not len(cache):
    print(f'{cache[i][0]}:{"#"*cache[i][1]}')

    # print('{0:>{}}: {1}'.format(cache[i][0], "#"*cache[i][1]))
    # print('{0:<9} {2}'.format('{0}-{1}:'.format(cache[i][0]), '#'*cache[i][1]))
    i += 1
