"""
Hash Tables
___________

What they solve

standard array seach O(n)

Main hash table operations: GET PUT DELETE

"""
#  Naive hashing function -- do not use in production
hash_data_size = 8

hash_data = [0] * hash_data_size


def hash_funciton(s):
    bytes_list = s.encode()

    total = 0

    for b in bytes_list:
        total += b
    return total


def get_index(s):
    hash_value = hash_funciton(s)
    return hash_value % hash_data_size


def put(k, v):
    # for the given key, store a value in the hash table
    index = get_index(k)
    hash_data[index] = v


def get(k):
    index = get_index(k)
    return hash_data[index]


print(hash_data)
# print(get_index('Michael'))
# print(get_index('Goats'))
# print(get_index('Gtoas'))
index = get_index('Michael')
# hash_data[index] = 'Hello, world!'
print(index)
print(get('Beej!'))
# put('Beej', 'Hello, world!')
# print(hash_data)

put('Beej', 'Hello again!')

print(hash_data)
