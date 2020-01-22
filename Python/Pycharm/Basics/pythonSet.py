print("Python sets are unordered collection of items which are not indexed.")
print("Items added to sets cannot be modified but new items can be added to the set.")
print("The items added to set cannot be accessed via index.")

fruit_set = {"apple", "banana", "mango"}
print(fruit_set)
fruit_set.add("pineapple")
print(fruit_set)

print("Update method can be used to add a collection of items to a set.")
fruit_set.update({"orange", "guava"})
print(fruit_set)

print(
    "The total number of items in the fruit-set {0} is {1}".format(fruit_set, len(fruit_set)))

print("The remove method is used to remove an item from a set. If the item is not present it throws an error of type KeyError.")
print("Removing Banana")
fruit_set.remove("banana")
print("Updated fruit set : " + str(fruit_set))
print("Removing Banana Again will throw a KeyError:banana in the console")
# fruit_set.remove("banana")

fruit_set.discard("banana")
fruit_set.discard("mango")
print("Updated fruit set after discarding mango is : " + str(fruit_set))
print("Updated fruit set after discarding banana again is : " + str(fruit_set))

print("\nDiscard method does not throw any error if the item is not found in the set.")
fruit_set.add("mango")
fruit_set.add("mango")
print("Updated fruit set after adding 2 mangoes is : " + str(fruit_set))
print("\nEven though we can add multiple items in a set, the set does not allow duplicate items.")
print("\nAfter adding multiple mango we still have only a single mango in the set.")

print("\nPOP method in set removes the last item of the set. The count also reduces by 1.")
print("Fruit Set : " + str(fruit_set))
fruit = fruit_set.pop()
print("The fruit list after removal of {0} is {1}".format(fruit, fruit_set))

print("The UNION method is used to join two sets similar to the update() method.")
print("\nThe difference between Union() and Update() method is that Union creates a new set with the items of both sets.")
print("\nUpdate method adds the set to the other set and does not create a new set.")

print("Intersection method returns the intersection of two sets")
company_set = {"apple", "microsoft", "google"}
print("The instersection set of the company set and fruit set is {0}".format(
    company_set.intersection(fruit_set)))
print("Company Set : " + str(company_set))

print("Intersetion Update method updates the set with the intersection element and removes all the elements which are not present")
company_set_backup = company_set.copy()
print("Company Set backup " + str(company_set_backup))
print("Running intersection update on company set over fruit set")
company_set_backup.intersection_update(fruit_set)
print("The updated company set is : "+str(company_set_backup))
print("Intersection update modifies the set on which it is run.")

print("\nIsDisjoint method of set returns TRUE if the sets have NO intersection.")
print(company_set)
print(fruit_set)
print(company_set.isdisjoint(fruit_set))


print("""\nsymmetric_difference() method returns all the members of the set which are not a part of the other set.
In other words, it returns the difference of the items in the set.
""")
print("The symmetric difference between the company set and fruit set are : " +
      str(company_set.symmetric_difference(fruit_set)))
