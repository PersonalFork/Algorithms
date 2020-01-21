print("Testing Data Types")
i = 10
# print(type(i))

j = "Test"
# print(type(j))

# print(j == i)

a, b, c = "Hello", "Test", 10
print(a)
print("DEL deletes a variable")
del a
# print(b, c)

# Multiline strings
str_test = """This is a multiline string written in 
Python as a programming language."""
# print(str)

str_test = "One Two Three"
# print("Printing : " + str[1])
# print("Printing Substring from 0th to 5th Index : " + str[0:5])
# print("Printing Substring from 5th to end : " + str[4:])
# print("Print String 5 times : " + str*5)
print("Print String from Reverse [-4] : " + str_test[-4])
print("Print String from Reverse [-4:-1]: " + str_test[-4:-1])
print("Print Length of String : " + len(str_test).__str__())

print("Trimming is done using Strip Method")
str_test += "  "
print(str_test + "Length : " + str(len(str_test)))
print("Trimming...")
str_test = str_test.strip()
print(str_test + "Length : " + str(len(str_test)))

print("upper() method converts the string in upper case.")
str_test = str_test.upper()
print(str_test)

print("lower() method converts the string in lower case")
str_test = str_test.lower()
print(str_test)

print("The replace method replaces a character with a different one.")
print(str_test.replace("o", "N"))

print("Split method splits a string by some specified character")
split_str = str_test.split(" ")
print(type(split_str))
print(split_str)

print("In is used for contains e.g. Test in 'Test is today'")
is_two_present = 'two' in str_test
print("String is : " + str_test)
print("Is two present : " + str(is_two_present))
is_one_present = 'One' in str_test
print("Is One present : " + str(is_one_present))

print("\nText formatting")
print("Is One present {0},{1},{0}".format(is_one_present, is_two_present))

str_test = str_test.lower()
print("In Lower Case : {0}".format(str_test))
print("In Sentence Case : {0}".format(str_test.capitalize()))
print("The center method centers the string by creating a string of the specified length and then placing the specified string in the center")
print("Centered String : {0}".format(str_test.center(50)))

print("\nPrinting escape characters")
print("This is printing after correcting the spelling of \"Pringing\" to Printing")

print("The find method finds the occurrence of the string/char and returns the index.")
print("Finding the string One")
print(str_test.find("ne"))
print("The difference between find and index is that Index method throws an exception if the string is not found in the string.")

print("regular expression and pattern matching")
str_int = "111111"
print("Print if the string {0} is all numeric : {1}".format(
    str_int, str_int.isnumeric()))

str_int = "abc1"
print("Print if the string {0} is all numeric : {1}".format(
    str_int, str_int.isnumeric()))

print("Join String is equivalent to String.Join method in .NET ")
str_list = str_test.split(" ")
items = ",".join(str_list)
print(items)