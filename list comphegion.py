if __name__ == '__main__':
    x = int(input())  # Input for x
    y = int(input())  # Input for y
    z = int(input())  # Input for z
    n = int(input())  # Input for n

    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    print(result)