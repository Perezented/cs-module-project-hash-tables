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


"""
Collision resolution by chaining
________________________________

Make our array of slots into an array of linked lists

Each linked list node is a HashTableEntry

Put
___

slot
index   Chain (linked list)
_____   ___________________
0   =>  None
1   =>  None
2  =>  None
3   =>  None
4   =>  None

put("foo", 12)  # hashes to 1

1. figure out the index
        1
2. search the linked list to see if the key is already there. 
        it is not
2a. If the key is there, overwrite the value
2b. If not there, create a new HastTableEntry and insert it in the list

Get
___

1. Figure out the index for the key
2. Search the linked list at the index for the HashTableEntry that matches the key
3. Return thge value for the entry, or None if not found

Delete
______

1. Figure out the index for the key
2.
Search the linked list at the index for the HashTableentry that matches the key 
2a. If found, delete the entry from the linked list -- return the value
2b. If not found, return None




"""
