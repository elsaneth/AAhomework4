MAX = 10
array = [[False for column in range(2)] for row in range(MAX + 1)]

def search(X):
    if X >= 0:
        return array[X][0], X
    X = abs(X)
    return array[X][1], X

def insert(list, length):
    for i in range(length):
        if list[i] >= 0:
            array[list[i]][0] = True
        else:
            abs_i = abs(list[i])
            array[abs_i][1] = True

def print_array_list():
    for i, row in enumerate(array):
        print(f"Index {i}: {row}")

if __name__ == "__main__":
    list = [-1, 9, -8, -5, -2, 5, 0]
    length = len(list)
    insert(list, length)
    X = -5
    is_present, index = search(X)
    if is_present:
        print(f"{X} is present at index {index}")
    else:
        print(f"{X} is not present")

    print("\nFull array list for debugging: ")
    print_array_list()

