# FIFO Page Replacement in Python

frames = int(input("Enter number of frames: "))
n = int(input("Enter number of pages: "))

print("Enter the page reference string:")
pages = list(map(int, input().split()))

temp = [-1] * frames
page_faults = 0
j = 0

print("\nPage\tFrames\n")

for i in range(n):
    flag = 0

    # Check if page already exists in frames
    for k in range(frames):
        if temp[k] == pages[i]:
            flag = 1
            break

    # If page not found → Page Fault
    if flag == 0:
        temp[j] = pages[i]
        j = (j + 1) % frames
        page_faults += 1

    # Print current state
    print(pages[i])
    for k in range(frames):
        if temp[k] != -1:
            print(temp[k])
        else:
            print("-")
    print()

print(f"\nTotal Page Faults = {page_faults}")
