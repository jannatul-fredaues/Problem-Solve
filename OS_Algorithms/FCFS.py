n = int(input("Enter the number of processes: "))

pid = list(map(int, input("Enter process IDs:\n").split()))
bt = list(map(int, input("Enter burst times:\n").split()))
at = list(map(int, input("Enter arrival times:\n").split()))

st = [0] * n
ct = [0] * n
wt = [0] * n
tat = [0] * n

# Stable sort by arrival time (same logic as C)
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if at[j] < at[min_idx]:
            min_idx = j

    if min_idx != i:
        at[i], at[min_idx] = at[min_idx], at[i]
        bt[i], bt[min_idx] = bt[min_idx], bt[i]
        pid[i], pid[min_idx] = pid[min_idx], pid[i]

# First process
st[0] = at[0]
ct[0] = st[0] + bt[0]
tat[0] = ct[0] - at[0]
wt[0] = tat[0] - bt[0]

# Remaining processes
for i in range(1, n):
    if ct[i - 1] <= at[i]:
        st[i] = at[i]
    else:
        st[i] = ct[i - 1]

    ct[i] = st[i] + bt[i]
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

# Output
total_wt = sum(wt)
total_tat = sum(tat)

print("\nPID\tAT\tBT\tST\tCT\tWT\tTAT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{st[i]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")

print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
print(f"Average Turnaround Time = {total_tat / n:.2f}")
