if __name__ == '__main__':
    n = int(input())

    #This .splits() use for split the string by spaces and makes a list of strings
    #map() applies a function to every item in the list
    a = list(map(int, input().split())) 
   
    
    # Remove duplicate scores
    b = list(set(a))

    # Sort the list
    b.sort()

    # Print the second highest score
    print(b[-2])