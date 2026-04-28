list1=["apple","banana","cherry"]
list2=[1,5,7,9,3]
list3=[True,False,False]
list4=["abc",34,True,"male"]
list5 = "apple"
string1="apple"
print(list1[0]) # This will print the first element of the list, which is "apple"
print(string1[0]) # This will print the first character of the string, which is "a")



print(list1[1-:-2]) # This will print the second and third elements of the list, which are "banana" and "cherry"
print(list1[-1]) # This will print the last element of the list, which is "cherry"
print(list1[-1:-2:-1]) 
print(list1 + ["tomato", 50])
print(list1 * 2) # This will print the list twice, which is ["apple", "banana", "cherry", "apple", "banana", "cherry"]
print(len(list1)) # This will print the length of the list, which is 3
list1[0] = "grape" # This will change the first element of the list to "grape"
print(list1) # This will print the modified list, which is ["grape", "banana", "cherry"]
list1.append("orange") # This will add "orange" to the end of the list

list1.clear() # This will remove all the elements from the list
print(list1) # This will print an empty list, which is []
 
list1.count("banana") # This will count the number of times "banana" appears in the list, which is 0
list1.extend(["grape", "melon"]) # This will add "grape" and "melon" to the end of the list
print(list1) # This will print the modified list, which is ["grape", "melon"]


list1.index("grape") # This will return the index of the first occurrence of "grape" in the list, which is 0
print(list1) # This will print the list, which is ["grape", "melon"]

list1.insert(1, "kiwi") # This will insert "kiwi" at index 1 in the list
print(list1) # This will print the modified list, which is ["grape", "kiwi", "melon"]

list1.pop() # This will remove the last element from the list, which is "melon"
print(list1) # This will print the modified list, which is ["grape", "kiwi"]

list1.remove("grape") # This will remove the first occurrence of "grape" from the list
print(list1) # This will print the modified list, which is ["kiwi"]

list1.reverse() # This will reverse the order of the elements in the list
print(list1) # This will print the modified list, which is ["kiwi"]

list1.sort() # This will sort the elements of the list in ascending order
print(list1) # This will print the modified list, which is ["kiwi"]
