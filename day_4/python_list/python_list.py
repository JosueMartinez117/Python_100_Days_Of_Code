'''
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data.

Example:

Different Data Types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

List items can be of any data type:
list = ["abc", 34, True, 40, "male"]

Python Collections:
The other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#Store many peaces of data.
states_of_mexico = ["CDMX", "Jalisco", "Yucatan", "Sonora", "Chihuaha"]
print(f"Original list of states_of_mexico {states_of_mexico}")
'''
Index
Why the first Index is Zero? 
This is because in Python you count from zero when indexing lists and so index 1 refers to the second item in the list. 
To get the first item you must use the index 0 . This "zero-indexing" is very common and is used by most programming languages.
'''
print(states_of_mexico[0])
#output: CDMX

fruits = ["Cherry", "Apple", "Pear"]
print(fruits[1])
#output: Apple

#Negative and Positive Indexes
#When negative indexes are used, "it starts counting from the end"
print(states_of_mexico[-1])
#output: Chihuaha
print(states_of_mexico[-2])
#output: Sonora

print(states_of_mexico[2])
#output: Yucatan

#How to write / modify data inside the list? 
states_of_mexico[1] = "Sinaloa"
print(f"List updated: {states_of_mexico}")
#Output: Sinaloa, Jalisco was replaced by Sinaloa in the list

#How to add a new item at the end of the list? 
#You can use "append" -> Append object to the end of the list.
#list.append(x)
states_of_mexico.append("Oaxaca")
print(f"List with new state added in the end of the list: {states_of_mexico}")

#list.extend(iterable)
#You need to create a short list using squirt brackets
states_of_mexico.extend(["Veracruz" , "Chiapas"])
print(f"List exteded adding two new states {states_of_mexico}")
