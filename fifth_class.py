# my_diction = {"Pet": "Dog", "Colour": "Brown"}
# my_diction["Colour"] = "Black"
# print(my_diction)

# print(my_diction["Pet"])
# print(my_diction.get("Pet"))
# print(my_diction.get("Country", "Nigeria"))

# my_diction["Country"] = "United Kingdom"
# print(my_diction)

# print(my_diction.copy())
# print(my_diction.keys())
# print(my_diction.values())
# print(my_diction.items())

# my_dict = {"Name": "Jerry", "Courses": ["Data science", "Backend"], "Scores": {"Data science": 20, "Backend": 15.7,},}
# course = input('Kindly select a course: ')
# score = input('Please enter your score: ')
# my_dict["Courses"].append(course)
# my_dict["Scores"][course] = score
# print(my_dict)

# my_dictionary = {
#     "name": "John",
#     "gender": "MALE",
# }

# my_dictionary.update({'key':'value'})
# list_of_tuples = [("John", "Abuja"), ("Nigeria", "Canada")]

# my_dictionary.update(list_of_tuples)
# print(my_dictionary)

# my_dict = {"Name": "Jerry", "Courses": ["Data science", "Backend"], "Scores": {"Data science": 20, "Backend": 15.7,},}
# a = my_dict.pop("Name")
# print(a)

# var = my_dict.pop("Scores")
# print(var)
# print(my_dict)
# my_dict.update({"Result": var})
# print(my_dict)
# my_dict["Result"] = var
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# print(type(my_dict["Scores"]))

# print(type(int("100")))
# print(type(my_dict.keys()))
# print(type(list(my_dict.keys())))
# print(type(my_dict))
# a = list(my_dict)
# print(a)

# sampleDict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500}
# }
# sampleDict['emp3']['salary'] = 8500
# print(sampleDict)

# users = {}
# first_name = input('Please enter your firstname: ')
# last_name = input('Please enter your lastname: ')
# username = first_name+last_name
# users[username] = {}
# users[username]['firstname'] = first_name
# users[username]['lastname'] = last_name
# print(users)

# mylist = [2, 2, 4, 6, 7, 2, 4, 4, 3, 6, 2, 1]
# my_list = set(mylist)
# print(my_list)
# mylist1 = list(my_list)
# mylist1.sort()
# print(mylist1)

# list1 = ['11', '55', '33']
# list2 = list1[0]+list1[1]+list1[2]
# list3 = int(list2)
# print(list3)

# list_2 = "".join(list1)
# list_3 = "".join(list_2)
# print(int(list_3))

# tuple1 = (False, 'True', 100, 22.4, "Yes", 18)
# a, b, c, d, e, f = tuple1
# print(f)

# tuple_1 = ("u", "n", "i", "v", "e", "l", "c", "i", "t", "y")
# tuple_2 = tuple_1[0]+tuple_1[1]+tuple_1[2]+tuple_1[3]+tuple_1[4]+tuple_1[5]+tuple_1[6]+tuple_1[7]+tuple_1[8]+tuple_1[9]
# tuple_3 = str(tuple_2)
# print(tuple_3)

a = list(tuple_1)
b = list(a)
c = ''.join(b)
print(type(c))
print(c)