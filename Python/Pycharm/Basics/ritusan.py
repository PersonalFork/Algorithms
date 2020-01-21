fruits = ["Apple", "Mango", "Oranges"]
fruits = []
print("The formatted string is {0}".format(", ".join(fruits)))

# Apple, Mango, Oranges
test = ""
for li in fruits:
    test = test + li + ", "
print(test[0:-2])

first_name = "Rituparna"
last_name = "bhattacharya"
age = 20

print("First Name : " + first_name +
      " | Last Name : " + last_name.upper() + " | Age : " +
      str(age) + ". " + first_name
      + " " + last_name + " is a student")

formatted_string = "First Name : {0} | Last Name : {1} | Age : {2}. {0} {1} is a student. ".format(
    first_name.upper(), last_name.upper(), age)
print(formatted_string)

full_name = first_name + " " + last_name
print(full_name.title())

# Rituparna Bhattacharya
print(first_name.capitalize() + " " + last_name.capitalize())

pax_list = ["Jahso", "Ritu"]
if(bool(len(pax_list))):
    print("Total Passengers : " + str(len(pax_list)))

sentence = "this is a test sentence.i am hello world."
sentence_split = sentence.split(".")
print(sentence_split)


def lmbda(x): return x.capitalize()


map_lmbda = map(lmbda, sentence_split)
final_string = ".".join(map_lmbda)
print(final_string)

if(bool(fruits)):
    # print("Printing fruits.")
    for fruit in fruits:
        # print(fruit)
        pass


def square(x, y):
    return x*y


integer_list_1 = [10, 20, 30]
integer_list_2 = [2, 4]

print(list(map(square, integer_list_1, integer_list_2)))
