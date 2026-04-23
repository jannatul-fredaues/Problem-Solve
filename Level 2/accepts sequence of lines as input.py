# Question: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#  Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Get the input from the user
lines = []
print("Enter lines of text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
# Convert each line to uppercase
uppercase_lines = [line.upper() for line in lines]
# Print the uppercase lines
for line in uppercase_lines:
    print(line)

    