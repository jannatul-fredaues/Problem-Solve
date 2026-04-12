# Priority Scheduling (Non-Preemptive) in Python

n = int(input("Enter number of processes: "))

pid = []
at = []
bt = []
pr = []
wt = [0] * n
tat = [0] * n
completed = [0] * n

# Input
for i in range(n):
    pid.append(i + 1)
    print(f"\nProcess {pid[i]}:")

    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))
    pr.append(int(input("Priority (lower value = higher priority): ")))

time = 0
done = 0
total_wt = 0
total_tat = 0

# Scheduling
while done < n:
    idx = -1
    highest_priority = float('inf')

    # Find highest priority process
    for i in range(n):
        if at[i] <= time and completed[i] == 0:
            if pr[i] < highest_priority:
                highest_priority = pr[i]
                idx = i
            elif pr[i] == highest_priority:
                if idx == -1 or at[i] < at[idx]:
                    idx = i

    if idx != -1:
        time += bt[idx]

        tat[idx] = time - at[idx]
        wt[idx] = tat[idx] - bt[idx]

        total_wt += wt[idx]
        total_tat += tat[idx]

        completed[idx] = 1
        done += 1
    else:
        time += 1  # CPU idle

# Output
print("\nPID\tAT\tBT\tPR\tWT\tTAT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{pr[i]}\t{wt[i]}\t{tat[i]}")

print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
print(f"Average Turnaround Time = {total_tat / n:.2f}")