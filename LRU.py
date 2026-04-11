frames = int(input("Enter number of frames: "))
n = int(input("Enter number of pages: "))

pages = list(map(int, input("Enter page reference string:\n").split()))

temp = [-1] * frames      # Frames
recent = [0] * frames     # Track recent use

page_faults = 0

print("\nPage\tFrames\n")

for i in range(n):
    flag1 = 0
    flag2 = 0

    # Check if page already exists (HIT)
    for j in range(frames):
        if temp[j] == pages[i]:
            flag1 = 1
            flag2 = 1
            recent[j] = i   # update recent use
            break

    # If MISS, check for empty frame
    if flag1 == 0:
        for j in range(frames):
            if temp[j] == -1:
                temp[j] = pages[i]
                recent[j] = i
                page_faults += 1
                flag2 = 1
                break

    # If MISS and no empty frame → replace LRU
    if flag2 == 0:
        min_val = recent[0]
        pos = 0

        for j in range(1, frames):
            if recent[j] < min_val:
                min_val = recent[j]
                pos = j

        temp[pos] = pages[i]
        recent[pos] = i
        page_faults += 1

    # Print frames
    print(pages[i])
    for k in range(frames):
        if temp[k] == -1:
            print("-")
        else:
            print(temp[k])
    print()

print("Total Page Faults =")
print(page_faults)