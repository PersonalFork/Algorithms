print(str(1 == 2))

print("""Any object can be passed to the bool() function. 
For an empty list,tuple,string it is always false. For non-zero integers it is false, otherwise true.
""")

obj = ()
print("Object {0} | Type : {1} | IsTrue : {2}".format(
    obj, type(obj), bool(obj)))
obj = ("India", "US", "Russia")
print("Object {0} | Type : {1} | IsTrue : {2}".format(
    obj, type(obj), bool(obj)))

obj_int = 10
print("Int {0} | True : {1}".format(obj_int, bool(obj_int)))

obj_int = 0
print("Int {0} | True : {1}".format(obj_int, bool(obj_int)))
