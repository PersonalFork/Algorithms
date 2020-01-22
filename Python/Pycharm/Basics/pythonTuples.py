print("Python Tuples are UNCHANGEABLE ordered collection of items")
print("They are written with () brackets")

fruit_tuple = ("Mango", "Apple", "Orange")
print(fruit_tuple)

print("Fruit_Tuple[0] : " + str(fruit_tuple[0]))
print("Fruit_Tuple[-1] : " + str(fruit_tuple[1]))

print("As tuples are unchangeable, they cannot be modified. Attempt will result in a TypeError.")
# fruit_tuple[0]="Kiwi"

print("To change a tuple, we need to create a list out of it and then modify the list.")
fruit_list = list(fruit_tuple)
fruit_list[0] = "Kiwi"
print("Fruit List modified from the tuple : " + str(fruit_list))

print("One Item tuple requires an extra comma after the first item to qualify it as a tuple.")
location_tuple = ("Bangalore")
print("Declaring a tuple with a single element without a comma like this location_tuple = (\"Bangalore\") will result in creation of object of type string")
print("Location Tuple : {0} | Type : {1}".format(
    location_tuple, type(location_tuple)))

location_tuple = ("Delhi",)
print("Location Tuple : {0} | Type : {1}".format(
    location_tuple, type(location_tuple)))

print("Joining tuples can be done simply using the concatenation + operator. The result is also a tuple")
new_tuple = location_tuple+fruit_tuple
print(
    "New Tuple location_tuple+fruit_tuple : {0} | type {1}".format(new_tuple, type(new_tuple)))
print("A list and tuple cannot be added. It will result in a type error (TypeError: can only concatenate list (not \"tuple\") to list")
# new_tuple = fruit_list + fruit_tuple

print("Del is used to delete a tuple from memory")
del(new_tuple)
print("Deleting new_tuple")
print(new_tuple)
