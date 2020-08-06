l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 4, 5] * 100000000

ht = {}
for x in l:
    ht[x] = True

# for n1 in l:  # 0(n)
#     for n2 in l:  # 0(n)
#         if n1 == n2:  # 0(1)
#             print('Duplicate!!')


def is_in_list(n):
    # for x in l "
    # if n == x:
    #     return True
    # return False

    return n in ht


for i in range(1000):
    print(is_in_list(i))
