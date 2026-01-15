def split_and_join(line):
    # Split the input string 'line' by space delimiter into a list of words
    words_list = line.split(" ") 
    
    # Join the words in the list using a hyphen '-' as the delimiter
    joined_string = "-".join(words_list)
    
    # Return the newly formed string
    return joined_string

if __name__ == '__main__':
    # The 'if __name__ == "__main__":' block is provided by HackerRank to handle input/output
    line = input()
    result = split_and_join(line)
    print(result)
