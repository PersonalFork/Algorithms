# print("Python list is an ordered collection which can be changed. List allows presence of duplicate items in it.")
# print("Tuple is an ordered collection which cannot be changed. Tuple allows presence of duplicate items in it.")
# print("Set is a collection which is UN-ORDERED and unindexed. Set does not allows duplicate items in it.")
# print("Dictionary is a collection which is UN-ORDERED and INDEX, which can be changed. Dictionary does not allow duplicate members.")

fruit_list = ["Apple", "Mango", "Banana", "Orange", "Pineapple"]

print("This is a list : " + str(fruit_list))

print("The first item of the list {0} is {1}".format(
    fruit_list, fruit_list[0]))
print("The last item of the list {0} is {1}".format(
    fruit_list, fruit_list[-1]))
print("The first to third item of the list {0} is {1}".format(
    fruit_list, fruit_list[0:2]))
print("The last to third item of the list {0} is {1}".format(
    fruit_list, fruit_list[-3:-1]))
print("List can be modified. The third item of the list has been modified to Strawberry now")
fruit_list[2] = "Strawberry"
print(fruit_list)

print("Printing the fruit list one by one.")
for fruit in fruit_list:
    print(fruit)
    pass

print("Check if apple is in list")
print("Apple is in List ? {0}".format("Apple" in fruit_list))

print("Items can be added to a list by using append() method")
fruit_list.append("Guava")
print("Total items in the fruit_list {0} is {1} ".format(
    fruit_list, len(fruit_list)))

print("Items can be inserted in a list using the insert() method at a specified index")
fruit_list.insert(10, "Cherry")
print(fruit_list)
print("""If the index in the insert method is greater than the number of items in the list, 
then the item will be inserted as the last item in the list""")

print("Items can be removed from a list using the remove() method. The remove method accepts an item as a parameter")
print("Removing Strawberry")
fruit_list.remove("Strawberry")
print("The new list is " + str(fruit_list))


