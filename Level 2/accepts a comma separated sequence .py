# Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#  Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Get the input from the user

input_string = input("Enter a comma separated sequence of words: ")
# Split the input string into a list of words
words = input_string.split(",")
# Sort the list of words alphabetically
sorted_words = sorted(words)
# Join the sorted list of words back into a comma-separated string
output_string = ",".join(sorted_words)
# Print the sorted words
print(output_string)

