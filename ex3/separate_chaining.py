def hash_function(key, container_count):
    return key % container_count

def insert_item(table, key, container_count):
    index = hash_function(key, container_count)
    table[index].append(key)

def print_hash(table, container_count):
    for container_index in range(container_count):
        print(container_index, end="")
        for key in table[container_index]:
            print(f" --> {key}", end="")
        print()

if __name__ == "__main__":
    array = [32, 18, 45, 23, 50]

    container_count = 7

    hash_table = [[] for container_index in range(container_count)]

    # insert the keys into the hash table
    for key in array:
        insert_item(hash_table, key, container_count)

    print_hash(hash_table, container_count)



