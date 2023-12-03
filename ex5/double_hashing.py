def double_hash_search(hash_table, key):
    size = len(hash_table)
    prime = 7

    def hash_function1(key):
        return key % size

    def hash_function2(key):
        return prime - (key % prime)

    attempt = 0
    initial_position = hash_function1(key)

    while attempt < size:
        index = (initial_position + attempt * hash_function2(key)) % size

        if hash_table[index] is None:
            print(f"Hash Table: {hash_table}")
            return False, None

        if hash_table[index] == key:
            print(f"Hash Table: {hash_table}")
            return True, index
        attempt += 1

    print(f"Hash Table: {hash_table}")
    return False, None

hash_table_size = 10
hash_table = [None] * hash_table_size

keys = [-1, 9, -8, -5, -2, 5, 0]

for key in keys:
    insert_attempt = 0
    while insert_attempt < hash_table_size:
        insert_index = (key + insert_attempt * (7 - (key % 7))) % hash_table_size
        if hash_table[insert_index] is None:
            hash_table[insert_index] = key
            break
        insert_attempt += 1

search_key = 5
is_present, index = double_hash_search(hash_table, search_key)

if is_present:
    print(f"{search_key} is present at index {index}")
else:
    print(f"{search_key} is not present")