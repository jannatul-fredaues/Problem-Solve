my_set= {1, 2, 3, 4, 5}
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0]) # This will print the first element of the tuple, which is
# 1
print(my_tuple[1:4]) # This will print the second, third and fourth elements of the tuple, which are 2, 3 and 4
print(my_tuple[-1]) # This will print the last element of the tuple, which is 5
print(my_tuple[-3:-1]) # This will print the third and fourth elements of the tuple, which are 3 and 4
print(my_tuple + (6, 7)) # This will print the tuple with the new elements added, which is (1, 2, 3, 4, 5, 6, 7)
print(my_tuple * 2) # This will print the tuple twice, which is (1      , 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(len(my_tuple)) # This will print the length of the tuple, which is 5  
my_tuple[0] = 10 # This will raise an error because tuples are immutable, which means that you cannot change the elements of a tuple after it has been created

