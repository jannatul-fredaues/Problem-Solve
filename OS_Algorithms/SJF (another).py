# SJF (Non-Preemptive) Scheduling in Python

n = int(input("Enter number of processes: "))

pid = list(map(int, input("Enter Process IDs: ").split()))
bt = list(map(int, input("Enter Burst Times: ").split()))
at = list(map(int, input("Enter Arrival Times: ").split()))

wt = [0] * n
tat = [0] * n
ct = [0] * n
visited = [0] * n

completed = 0
time = 0
avgWT = 0
avgTAT = 0

while completed != n:
    smallest = -1

    # Find process with shortest burst time among arrived ones
    for i in range(n):
        if not visited[i] and at[i] <= time:
            if smallest == -1 or bt[i] < bt[smallest]:
                smallest = i

    # If no process has arrived yet → CPU idle
    if smallest == -1:
        time += 1
        continue

    # Execute process
    time += bt[smallest]
    ct[smallest] = time
    tat[smallest] = ct[smallest] - at[smallest]
    wt[smallest] = tat[smallest] - bt[smallest]

    visited[smallest] = 1
    completed += 1

# Output
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
    avgWT += wt[i]
    avgTAT += tat[i]

avgWT /= n
avgTAT /= n

print(f"\nAverage Waiting Time: {avgWT:.2f}")
print(f"Average Turnaround Time: {avgTAT:.2f}")
