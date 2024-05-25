#1
my_dict = {"Nastya": 23, "Ivan": 42, "Gena": 17}
print("Dictionary: ", my_dict)
print("Age Gena: ", my_dict["Gena"])
my_dict['Dasha'] = 18
print("Age Dasha: ", my_dict['Dasha'])
my_dict["Roma"] = 13
print(my_dict.get("Lena", "Absent"))
print("Modified dictionary: ",  my_dict)
a = my_dict.pop("Nastya")
print("Delated: ", a )
print("Next: ", my_dict)
#2
my_set = {1, 2, 3, 4, "Apple", 2, 1, "Orange", 3, 4.5, 4.5, "Apple"}
print(my_set)
print(my_set.add( 5))
print(my_set.add( 12))
print(my_set)
print(my_set.discard("Orange"))
print(my_set)



