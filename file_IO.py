# new_file = open("Filepath + filename", mode = "r")
# print(new_file.read())
# new_file.close


# my_file = open("favor.txt", mode = "w")

# my_file.write("This is another file\n" "This is a file\n" "This is not a file")
# my_file.writelines(['This is line 1\n', 'This is line 2\n', '\tThis is a tab.'])

# my_file = open("favor.txt", mode = "a")

# my_file.write("This is another file\n" "This is a file\n" "This is not a file")
# my_file.writelines(['This is line 1\n', 'This is line 2\n', '\tThis is a tab.'])

# my_file = open("favor.txt", mode = "r")

# texts = my_file.read()
# print(texts)

# texts = my_file.readlines()
# for text in texts:
#     print(text)

# with open('Mary.txt', 'w') as paul:
#     paul.write("My name is paul")

# paul.write("I have risen")

import ast
d = {
    "name":"paul"
}
with open('favor.txt', 'w') as paul:
    paul.write(f'{d}')

with open('favor.txt', 'r') as mercy:
    favour = mercy.read()
    a = ast.literal_eval(favour)
    print(type(a))

#     print(dict(favour))
#     print(favour)
# paul.write("I have risen")