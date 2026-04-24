# Banker's Algorithm in Python

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

# Allocation Matrix
print(f"Enter Allocation Matrix ({n} x {m}):")
allocation = []
for i in range(n):
    row = list(map(int, input().split()))
    allocation.append(row)

# Max Matrix
print(f"Enter Max Matrix ({n} x {m}):")
max_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    max_matrix.append(row)

# Available Resources
print(f"Enter Available Resources ({m}):")
available = list(map(int, input().split()))

# Need Matrix = Max - Allocation
need = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(max_matrix[i][j] - allocation[i][j])
    need.append(row)

finish = [0] * n
safe_sequence = []
count = 0

# Banker's Algorithm
while count < n:
    found = False

    for i in range(n):
        if finish[i] == 0:
            can_run = True

            for j in range(m):
                if need[i][j] > available[j]:
                    can_run = False
                    break

            if can_run:
                # Release resources
                for k in range(m):
                    available[k] += allocation[i][k]

                safe_sequence.append(i)
                finish[i] = 1
                count += 1
                found = True

    if not found:
        print("System is NOT in safe state.")
        exit()

# Output
print("System is in SAFE state.")
print("Safe Sequence:", end=" ")
for p in safe_sequence:
    print(f"P{p}", end=" ")
print()
