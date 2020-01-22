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

print("The last item can be removed from the list using the pop() method.")
last_fruit = fruit_list.pop()
print("The last fruit removed from the list is " + last_fruit)
print("The new list is " + str(fruit_list))
fruit_list.append(last_fruit)
print(
    "The last fruit {0} has been re-added using append() method : {1}".format(last_fruit, fruit_list))

print("The clear() method clears the list.")
print("The copy() method creates a copy of a list.")
copy_fruit_list = fruit_list.copy()
fruit_list.clear()
print("Actual fruit list is : " + str(fruit_list))
print("Copy of fruit list is : " + str(copy_fruit_list))
print("Another method of copying a list is using list(old_list). This creates a new list with the elements inside")
copy_fruit_list_new = list(copy_fruit_list)
print(copy_fruit_list_new)


print("Items of list can be added using the + operator")
domestic_animals = ["Cow", "Dog"]
wild_animals = ["Tiger", "Lion"]

print("Domestic animals : " + str(domestic_animals))
print("Wild animals : " + str(wild_animals))

print("Wild Animals + Domestic Animals : " +
      str(wild_animals+domestic_animals))

print("Wild Animals.extend(Domestic Animals) : " +
      str(wild_animals.extend(domestic_animals)))


print("Sorting a list can be done using the sort method in a list.")
copy_fruit_list.sort()
print(copy_fruit_list)
print("Default sorting will happen based on the value of the items in the list.")
print("To sort in reverse, we need to specify named parameter reverse=true in the arguments")
copy_fruit_list.sort(reverse=True)
print("Printing in reverse : " + str(copy_fruit_list))

print("Sorting can also be done by passing a lambda expression which returns a value")


def sortByLength(x):
    return len(x)


copy_fruit_list.sort(key=sortByLength, reverse=True)
print("Sorting by Length of item : " + str(copy_fruit_list))
