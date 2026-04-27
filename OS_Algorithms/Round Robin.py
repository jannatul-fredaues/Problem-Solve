n = int(input("Enter number of processes: "))

at = []
bt = []
rt = []
ct = [0] * n
tat = [0] * n
wt = [0] * n

for i in range(n):
    a, b = map(int, input(f"Enter Arrival Time and Burst Time for Process {i+1}: ").split())
    at.append(a)
    bt.append(b)
    rt.append(b)

tq = int(input("Enter Time Quantum: "))

queue = []
visited = [0] * n
done = [0] * n

# Find first arrival
min_at = at[0]
first = 0
for i in range(1, n):
    if at[i] < min_at:
        min_at = at[i]
        first = i

time = at[first]
queue.append(first)
visited[first] = 1

completed = 0

print("\nGantt Chart:\n|", end="")

while completed < n:
    if len(queue) == 0:
        # CPU idle case
        for i in range(n):
            if done[i] == 0:
                queue.append(i)
                visited[i] = 1
                time = at[i]
                break

    i = queue.pop(0)  # dequeue

    if rt[i] > tq:
        print(f" P{i+1} |", end="")
        time += tq
        rt[i] -= tq
    elif rt[i] > 0:
        print(f" P{i+1} |", end="")
        time += rt[i]
        ct[i] = time
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
        rt[i] = 0
        done[i] = 1
        completed += 1

    # Enqueue newly arrived processes
    for j in range(n):
        if at[j] <= time and rt[j] > 0 and visited[j] == 0:
            queue.append(j)
            visited[j] = 1

    # Re-enqueue current process if not finished
    if rt[i] > 0:
        queue.append(i)

# Output
avgWT = sum(wt) / n
avgTAT = sum(tat) / n

print("\n\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print(f"\nAverage Waiting Time = {avgWT:.2f}")
print(f"Average Turnaround Time = {avgTAT:.2f}")
